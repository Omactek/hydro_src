# riverapp/urls.py
from django.urls import path
from .views import station_data
from .views import water_level_chart, get_station_data, get_chart_data, metadata, get_dropdown_values, get_available_years

urlpatterns = [
    path('', metadata, name='dynamic_chart'),
]
