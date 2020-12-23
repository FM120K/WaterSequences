from django.shortcuts import render
from django.http import JsonResponse
from .models import SeawaterSample
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import SampleListSerializer, SampleCreateSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class sampleList(ListAPIView):
    queryset = SeawaterSample.objects.all()
    serializer_class = SampleListSerializer


class UpdateSample(UpdateAPIView):
    serializer_class = SampleCreateSerializer
    permission_classes = [IsAdminUser]


class SampleCreate (CreateAPIView):
    serializer_class = SampleCreateSerializer
    permission_classes = [IsAdminUser]

def sample_detail(request, sample_number):
    sample_object = SeawaterSample.objects.get(sampleNumber=sample_number)

    my_sample = {
        'sampleNumber': sample_object.sampleNumber,
        'depth': sample_object.depth,
        'sampleLabel': sample_object.sampleLabel,
        'sampleStation': sample_object.sampleStation,
        'sampleGPS_N': sample_object.sampleGPS_N,
        'sampleGPS_E': sample_object.sampleGPS_E,
        'sampleDate' : sample_object.sampleDate,
        'sampleTime' : sample_object.sampleTime,
        'sampleVolume': sample_object.sampleVolume,
        'storage': sample_object.storage,
        'processed': sample_object.processed,
        'processedVolume' : sample_object.processedVolume,
        'remainingVolume' : sample_object.remainingVolume,
        'extractionKit' : sample_object.extractionKit,
        'sampleDepth' : sample_object.sampleDepth,
        'sampleO2Level': sample_object.sampleO2Level,
        'sampleTemp' : sample_object.sampleTemp,
        'sampleSalinity' : sample_object.sampleSalinity,
        'airTempInShade' : sample_object.airTempInShade,
        'cloudCover' : sample_object.cloudCover,
        'windSpeed' : sample_object.windSpeed,
        'seaColor' : sample_object.seaColor,
        'tide' : sample_object.tide,
        'RH' : sample_object.RH,
        'windDirection' : sample_object.windDirection,
        'baromPressure' : sample_object.baromPressure,
        'waveHeight' : sample_object.waveHeight,
        'secchiDisk' : sample_object.secchiDisk,
        'TotalDepth' : sample_object.TotalDepth,
        'elutionVolume' : sample_object.elutionVolume,
        'Concentration' : sample_object.Concentration,
        'DNA_Concentration' : sample_object.DNA_Concentration,
        'Carb_Concentration' : sample_object.Carb_Concentration,
        'TotalYield' : sample_object.TotalYield,
        'F_readfile' : sample_object.F_readfile,
        'R_readfile' : sample_object.R_readfile,
        'Notes' : sample_object.Notes,
    }

    return JsonResponse(my_sample)
