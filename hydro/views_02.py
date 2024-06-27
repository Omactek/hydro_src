from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import ExtractYear
from .serializers import StationMetadataSerializer, ValuesMetadataSerializer, StationGeoSerializer
from hydro import models as hydro_models
from django.apps import apps
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db.models import F, Func, Max, Min
from datetime import date
from datetime import datetime
from .aggregates import Percentile
from rest_framework.exceptions import ValidationError
from .utils import prepare_data_for_chart

class ValuesMetadataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = hydro_models.ValuesMetadata.objects.all()
    serializer_class = ValuesMetadataSerializer

class StationMetadataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = hydro_models.StationMetadata.objects.all()
    serializer_class = StationMetadataSerializer

    @action(detail=True, methods=['get'])
    def values(self, request, pk=None):
        station = self.get_object()
        model = self.get_model_from_table(station.st_name)
        fields = [field.name for field in model._meta.fields]
        values = hydro_models.ValuesMetadata.objects.filter(django_field_name__in=fields)
        serializer = ValuesMetadataSerializer(values, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get']) #will need filtration based on values?
    def years(self, request, pk=None):
        station = self.get_object()
        model = self.get_model_from_table(station.st_name)
        years = sorted(model.objects.annotate(year=ExtractYear('date_time')).values_list('year', flat=True).distinct())
        return Response(years)
    
    @action(detail=False, methods=['get'])
    def geo(self, request):
        serializer = StationGeoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def get_model_from_table(table_name):
        for model in apps.get_models():
            if model._meta.db_table == table_name:
                return model
        raise ValueError('No model found with db_table {}!'.format(table_name))

@api_view(['GET'])
def chart_data(request, station_id, field, year):
    model = StationMetadataViewSet.get_model_from_table(station_id)
    year = int(year)
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)

    data = model.objects.filter(date_time__gte=start_date, date_time__lte=end_date).annotate(
        date=F('date_time'),
        value=F(field)
    ).values('date', 'value').order_by('date')
    return Response(data)

@api_view(['GET'])
def get_percentiles(request, station_id, field):
    model = StationMetadataViewSet.get_model_from_table(station_id)
    if field not in [f.name for f in model._meta.fields]:  #mitigating SQL injection risks
        raise ValidationError('error: Invalid field')
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' #check for custom header

    # Annotate month and calculate percentiles
    queryset = (model.objects
                .annotate(string_date_without_year=Func(
                    F('date_time'), function='to_char', template="%(function)s(date_trunc('month', %(expressions)s), 'MM-DD\"T\"HH24:MI:SS')"))
                .values('string_date_without_year')
                .annotate(
                    q10=Percentile(0.10, field),
                    q20=Percentile(0.20, field),
                    q30=Percentile(0.30, field),
                    q40=Percentile(0.40, field),
                    q50=Percentile(0.50, field), #median
                    q60=Percentile(0.60, field),
                    q70=Percentile(0.70, field),
                    q80=Percentile(0.80, field),
                    q90=Percentile(0.90, field))
                .order_by('string_date_without_year'))

    results = list(queryset)
    if is_ajax:  # Preparing data for chart
        results = prepare_data_for_chart(results)

    return Response(results)

@api_view(['GET'])
def dataseries(request, station_id, field):
    model = StationMetadataViewSet.get_model_from_table(station_id)
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')
    
    if start_date and end_date:
        print(start_date)
        queryset = model.objects.filter(date_time__gte=start_date, date_time__lte=end_date).annotate(
            date=F('date_time'),
            value=F(field)
        ).values('date', 'value').order_by('date')
    else: #will probably crash if opened through browser
        queryset = model.objects.annotate(
            date=F('date_time'),
            value=F(field)
        ).values('date', 'value').order_by('date')

    objects_with_field = model.objects.filter(**{f'{field}__isnull': False})
    objects_without_field = model.objects.filter(**{f'{field}__isnull': True}).values_list('date_time', flat=True)
    min_date = objects_with_field.aggregate(min_date=Min('date_time'))['min_date'].strftime('%d-%m-%Y')
    max_date = objects_with_field.aggregate(max_date=Max('date_time'))['max_date'].strftime('%d-%m-%Y')
    dates_without_field = [date.strftime('%d-%m-%Y') for date in objects_without_field]

    response_data = {
        "min_date": min_date,
        "max_date": max_date,
        "disable_dates": dates_without_field,
        "data": list(queryset)
    }
    return Response(response_data)

def chart_map(request):
    return render(request, 'chart_map.html')

def test(request):
    return render(request, 'test.html')