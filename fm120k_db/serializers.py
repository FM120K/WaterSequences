from rest_framework import serializers
from .models import SeawaterSample


class SampleListSerializer (serializers.ModelSerializer):
    class Meta:
        model = SeawaterSample
        fields = ['id', 'sampleLabel', 'depth']
