from django.shortcuts import render
from django.http import JsonResponse
from .models import SewageSample
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SampleListSerializer
# Create your views here.

class sampleList(ListAPIView):
        queryset = SewageSample.objects.all()
        serializer_class = SampleListSerializer



def sample_detail(request, sample_id):
        sample_object = SewageSample.objects.get(id=sample_id)
        my_sample = {
                'sampleNumber': sample_object.sampleNumber,
                'depth' : sample_object.depth,
                'sampleLabel': sample_object.sampleLabel,
                'sampleStation': sample_object.sampleStation
        }

        return JsonResponse(my_sample)
    