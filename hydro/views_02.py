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
from django.db.models import Count
import numpy as np
from django.db import connection

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
    # Construct SQL for calculating quartiles using percentile_cont in PostgreSQL
    sql = f'''
        WITH
            -- Query to fetch data for a specific year and parameter
            year_data AS (
                SELECT
                    EXTRACT(YEAR FROM date_time) AS YEAR,
                    date_time,
                    "{field}"
                FROM
                    {station_id}
                WHERE
                    EXTRACT(YEAR FROM date_time) = 2022  -- Replace with your desired year
            ),
            all_years_data AS (
                SELECT
                    EXTRACT(YEAR FROM date_time) AS year,
                    percentile_cont(0.25) WITHIN GROUP (ORDER BY "{field}") AS q1,
                    percentile_cont(0.5) WITHIN GROUP (ORDER BY "{field}") AS median,
                    percentile_cont(0.75) WITHIN GROUP (ORDER BY "{field}") AS q3
                FROM
                    {station_id}
                GROUP BY
                    year
            )
        -- Final query to combine the results
        SELECT
            yd.date_time,
            yd."{field}",
            ayd.q1,
            ayd.median,
            ayd.q3
        FROM
            year_data yd
            CROSS JOIN all_years_data ayd
        WHERE
            EXTRACT(YEAR FROM yd.date_time) = ayd.year
        ORDER BY
            yd.date_time;
    '''

    # Execute raw SQL query and fetch results
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

    # Prepare response data
    all_years_data = [
        {'date_time': row[0], field: row[1], 'q1': row[2], 'median': row[3], 'q3': row[4]}
        for row in rows
    ]

    return Response(all_years_data)


"""def chart_data_view(request):
    return render(request, 'test.html')

def map_view(request):
    return render(request, 'map.html')
""" #legacy
def chart_map(request):
    return render(request, 'chart_map.html')