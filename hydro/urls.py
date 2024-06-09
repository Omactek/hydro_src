# riverapp/urls.py
from django.urls import path, include
from .views import MyFormView
from rest_framework.routers import DefaultRouter
from .views_02 import StationMetadataViewSet, chart_data_view, chart_data

router = DefaultRouter()
router.register(r'stations', StationMetadataViewSet)

urlpatterns = [
    path('test_template/', MyFormView.as_view(), name='my_form_view'),
    path('', chart_data_view, name='chart_data_view'),
    path('api/', include(router.urls)),
    path('api/stations/<str:station_id>/data/', chart_data, name='chart-data'),
]