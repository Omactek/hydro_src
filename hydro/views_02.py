from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import ExtractYear
from .serializers import StationMetadataSerializer, ValuesMetadataSerializer
from hydro import models as hydro_models
from django.apps import apps
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db.models import F
from datetime import date

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

    @action(detail=True, methods=['get'])
    def years(self, request, pk=None):
        station = self.get_object()
        model = self.get_model_from_table(station.st_name)
        years = sorted(model.objects.annotate(year=ExtractYear('date_time')).values_list('year', flat=True).distinct())
        return Response(years)

    @staticmethod
    def get_model_from_table(table_name):
        for model in apps.get_models():
            if model._meta.db_table == table_name:
                return model
        raise ValueError('No model found with db_table {}!'.format(table_name))

@api_view(['GET'])
def chart_data(request, station_id):
    field = request.GET.get('field')
    year = int(request.GET.get('year'))

    model = StationMetadataViewSet.get_model_from_table(station_id)

    start_date = date(year - 1, 11, 1)
    end_date = date(year, 10, 30)

    data = model.objects.filter(date_time__gte=start_date, date_time__lte=end_date).annotate(
        date=F('date_time'),
        value=F(field)
    ).values('date', 'value').order_by('date')
    return Response(data)

def chart_data_view(request):
    return render(request, 'test.html')
