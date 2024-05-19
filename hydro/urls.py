# riverapp/urls.py
from django.urls import path
from .views import metadata

urlpatterns = [
    path('', metadata, name='test_template'), #tady je něco špatně
    path('dynamic_chart/', metadata, name='dynamic_chart'),
]
