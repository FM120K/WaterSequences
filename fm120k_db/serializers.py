from rest_framework import serializers
from .models import SewageSample

class SampleListSerializer (serializers.ModelSerializer):
    class Meta:
        model = SewageSample
        fields = ['id', 'sampleLabel', 'depth']