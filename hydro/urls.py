from django.urls import path, include
from .views import MyFormView
from rest_framework.routers import DefaultRouter
from .views_02 import StationMetadataViewSet, chart_data, ValuesMetadataViewSet, chart_map, get_percentiles, dataseries, test #legacy: , hart_data_view, , map_view

router = DefaultRouter()
router.register(r'stations', StationMetadataViewSet)
router.register(r'values', ValuesMetadataViewSet)

urlpatterns = [
    path('test_template/', MyFormView.as_view(), name='my_form_view'),
    #path('', chart_data_view, name='chart_data_view'), legacy
    path('api/', include(router.urls)),
    path('api/<str:station_id>/<str:field>/<str:year>/data/', chart_data, name='chart-data'),
    #path('map/', map_view, name='map'), legacy
    path('both/', chart_map, name='both'),
    path('api/<str:station_id>/<str:field>/percentiles/', get_percentiles, name='get_percentiles'),
    path('test/api/<str:station_id>/<str:field>/dataseries/', dataseries, name='get_dataseries'),
    path('test/', test, name='test'),
]