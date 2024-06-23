from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import ExtractYear
from .serializers import StationMetadataSerializer, ValuesMetadataSerializer, StationGeoSerializer
from hydro import models as hydro_models
from django.apps import apps
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db.models import F, Func, Value, FloatField
from datetime import date
from .aggregates import Percentile
from rest_framework.exceptions import ValidationError


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
def chart_data(request, station_id):
    field = request.GET.get('par')
    year = int(request.GET.get('year'))

    model = StationMetadataViewSet.get_model_from_table(station_id)

    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)

    data = model.objects.filter(date_time__gte=start_date, date_time__lte=end_date).annotate(
        date=F('date_time'),
        value=F(field)
    ).values('date', 'value').order_by('date')
    return Response(data)

@api_view(['GET'])
def all_years_data_query(request, station_id, field):
    model = StationMetadataViewSet.get_model_from_table(station_id)
    if field not in [f.name for f in model._meta.fields]: #mitigating sql injection risks
        raise ValidationError('error: Invalid field')

    queryset = (model.objects
                .annotate(month=Func(
                    F('date_time'), function='to_char', template="%(function)s(date_trunc('month', %(expressions)s), 'MM')"))
                .values('month')
                .annotate(
                    q20=Percentile(0.20, field),
                    q40=Percentile(0.40, field),
                    q50=Percentile(0.50, field),  #median
                    q60=Percentile(0.60, field),
                    q80=Percentile(0.80, field))
                .order_by('month'))

    return Response(queryset)

def chart_map(request):
    return render(request, 'chart_map.html')