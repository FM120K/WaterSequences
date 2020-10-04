from django.shortcuts import render
from django.http import JsonResponse
from .models import SeawaterSample
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import SampleListSerializer, SampleCreateSerializer
# Create your views here.

class sampleList(ListAPIView):
    queryset = SeawaterSample.objects.all()
    serializer_class = SampleListSerializer


class SampleCreate (CreateAPIView):
    serializer_class = SampleCreateSerializer
    


def sample_detail(request, sample_id):
    sample_object = SeawaterSample.objects.get(id=sample_id)
    my_sample = {
        'sampleNumber': sample_object.sampleNumber,
        'depth': sample_object.depth,
        'sampleLabel': sample_object.sampleLabel,
        'sampleStation': sample_object.sampleStation
    }

    return JsonResponse(my_sample)
