# riverapp/urls.py
from django.urls import path
from .views import MyFormView

urlpatterns = [
    path('test_template/', MyFormView.as_view(), name='my_form_view')
]