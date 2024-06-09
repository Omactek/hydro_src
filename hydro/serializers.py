from rest_framework import serializers
from hydro import models as hydro_models

class StationMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = hydro_models.StationMetadata
        fields = ['st_name', 'st_label']

class ValuesMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = hydro_models.ValuesMetadata
        fields = ['django_field_name', 'parameter', 'unit']
