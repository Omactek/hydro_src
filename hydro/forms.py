from django import forms
from hydro import models as hydro_models
from django.core.exceptions import ValidationError
from django.apps import apps
from django.db.models.functions import ExtractYear
import datetime


class ChartDataForm(forms.Form):
    station_name = forms.ChoiceField(choices=[(station.st_name, station.st_label) for station in hydro_models.StationMetadata.objects.all()], label="Select Station")
    value = forms.ChoiceField(choices=[(values.django_field_name, values.parameter) for values in hydro_models.ValuesMetadata.objects.all()], label="Select Value")
    station_name_change = forms.BooleanField(required=False, widget=forms.HiddenInput() )
    year = forms.ChoiceField(label="Select year", required=False)

    def __init__(self, *args, **kwargs): #what if i populate it all with one model?
        super(ChartDataForm, self).__init__(*args, **kwargs)
        current_year = datetime.date.today().year
        initial_years = [(str(year), year) for year in range(1980, current_year + 1)]
        self.fields['year'].choices = initial_years
        self.fields['year'].initial = '2008'

    def clean(self): 
        cleaned_data = super().clean()
        return cleaned_data
    
    def get_station_model(self):
        cleaned_data = self.cleaned_data #self.clean()
        station_selected = cleaned_data.get('station_name')
        station_selected = hydro_models.StationMetadata.objects.get(st_name=station_selected).st_name
        self.model = self.get_model_from_table(station_selected)
        return self.model

    def update_value_choices(self):
        self.clean() #is it needed?
        self.get_station_model()
        fields = [field.name for field in self.model._meta.fields]
        values = hydro_models.ValuesMetadata.objects.filter(django_field_name__in=fields)
        self.fields['value'].choices = [(v.django_field_name, v.parameter) for v in values]
        if self.cleaned_data['station_name_change'] == True:
            self.cleaned_data['value'] = self.fields['value'].choices[0][0]

    def update_year_choices(self):
        self.get_station_model()
        print(f"toto je model: {self.model}")
        queryset = self.model.objects.all()
        years = sorted(queryset.annotate(year=ExtractYear('date_time')).values_list('year', flat=True).distinct())
        choices = [(year, year) for year in years]  # Creating tuples of (year, year)
        self.fields['year'].choices = choices

    @staticmethod
    def get_model_from_table(table_name):
        for model in apps.get_models():
            if model._meta.db_table == table_name:
                return model
        else:
            raise ValueError('No model found with db_table {}!'.format(table_name))
