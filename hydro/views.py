from django.shortcuts import render
#from .models import ValuesMetadata, StationMetadata
from hydro import models as hydro_models
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.apps import apps
from django.db.models.functions import ExtractYear
from .forms import ChartDataForm
from django.views.generic.edit import FormView

class MyFormView(FormView):
    template_name = 'test_template.html'
    form_class = ChartDataForm
    success_url = 'succes/'

    def form_valid(self, form):
        form.is_valid()
        form.update_value_choices()
        form.update_year_choices()
        station_model = form.model
        station_name = form.cleaned_data['station_name']
        value = form.cleaned_data['value']
        year = form.cleaned_data['year']


        return self.render_to_response(self.get_context_data(
            form=form,
            station=station_name,
            station_model=station_model,
            value=value,
            success=True,
            year=year,
        ))
    def form_invalid(self, form):
        print("Form invalid, errors:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))