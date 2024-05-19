from django.shortcuts import render
from .models import ValuesMetadata, StationMetadata
from django.apps import apps

def metadata(request):
    #retrieve station names and labels from StationMetadata
    station_metadata = StationMetadata.objects.all()
    #retrieve values metadata from ValuesMetadata
    values_metadata = ValuesMetadata.objects.all()
    list = ["water_level", "air_temperature"]
    values_metadata = ValuesMetadata.objects.filter(parameter_abreviation_in_data_file__in=list)

    context = {
        'station_metadata': station_metadata,  #pass station metadata to the template
        'values_metadata': values_metadata, #pass values metadata to the template
    }

    return render(request, 'dynamic_chart.html', context)