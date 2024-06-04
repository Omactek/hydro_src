# riverapp/urls.py
from django.urls import path
from .views import metadata, ChartDataView, GetAvailableYearsView, MyFormView

urlpatterns = [
    path('test_template/', MyFormView.as_view(), name='my_form_view')
]
