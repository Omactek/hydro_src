from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StationMetadataViewSet, chart_data, ValuesMetadataViewSet, chart_map, get_percentiles, dataseries, test

router = DefaultRouter()
router.register(r'stations', StationMetadataViewSet)
router.register(r'values', ValuesMetadataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/stations/<str:station_id>/<str:field>/<str:year>/data/', chart_data, name='chart-data'),
    path('both/', chart_map, name='both'),
    path('api/stations/<str:station_id>/<str:field>/percentiles/', get_percentiles, name='get_percentiles'),
    path('api/stations/<str:station_id>/<str:field>/dataseries/', dataseries, name='get_dataseries'),
    path('test/', test, name='test'),
]