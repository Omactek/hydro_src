# riverapp/urls.py
from django.urls import path
from .views import metadata

urlpatterns = [
    path('', metadata, name='dynamic_chart'),
]
