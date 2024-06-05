from django import forms
from hydro import models as hydro_models
from django.core.exceptions import ValidationError
from django.apps import apps


class ChartDataForm(forms.Form):
    station_name = forms.ChoiceField(choices=[(station.st_name, station.st_label) for station in hydro_models.StationMetadata.objects.all()], label="Select Station")
    value = forms.ChoiceField(choices=[(values.django_field_name, values.parameter) for values in hydro_models.ValuesMetadata.objects.all()], label="Select Value")
    auto_submit = forms.CharField(max_length=255, required=False, widget=forms.HiddenInput())

    def clean(self): 
        cleaned_data = super().clean()
        return cleaned_data
    
    def get_station_model(self):
        cleaned_data = self.cleaned_data #self.clean()
        station_name = cleaned_data.get('station_name')
        station_name = hydro_models.StationMetadata.objects.get(st_name=station_name).st_name
        self.model = self.get_model_from_table(station_name)
        return self.model

    def update_value_choices(self):
        # This method updates the 'choices' attribute of the 'value' field
        self.clean()
        self.get_station_model()
        fields = [field.name for field in self.model._meta.fields]
        values = hydro_models.ValuesMetadata.objects.filter(django_field_name__in=fields)
        self.fields['value'].choices = [(v.django_field_name, v.parameter) for v in values]


    @staticmethod
    def get_model_from_table(table_name):
        for model in apps.get_models():
            if model._meta.db_table == table_name:
                return model
        else:
            raise ValueError('No model found with db_table {}!'.format(table_name))

