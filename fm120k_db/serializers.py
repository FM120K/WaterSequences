from rest_framework import serializers
from .models import SeawaterSample


class SampleListSerializer (serializers.ModelSerializer):
    class Meta:
        model = SeawaterSample
        fields = ['id', 'sampleLabel', 'depth']

class SampleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeawaterSample
        fields = ['sampleNumber', 'sampleVolume', 'depth', 'sampleLabel', 'sampleStation', 'storage', 'processed', 'processedVolume', 'remainingVolume', 'extractionKit', 'sampleDate', 'sampleTime', 'sampleGPS_N', 'sampleGPS_E', 'sampleDepth', 'sampleO2Level', 'sampleTemp', 'sampleSalinity', 'airTempInShade','cloudCover','windSpeed','seaColor','tide','RH', 'windDirection','baromPressure','waveHeight','secchiDisk','TotalDepth']
    