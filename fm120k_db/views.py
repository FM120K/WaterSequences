from django.shortcuts import render
from django.http import JsonResponse
from .models import SeawaterSample
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .serializers import SampleListSerializer, SampleCreateSerializer
# Create your views here.

class sampleList(ListAPIView):
    queryset = SeawaterSample.objects.all()
    serializer_class = SampleListSerializer


class SampleCreate (APIView):
    serializer_class = SampleCreateSerializer

    def post (self, request, *args, **kwargs):
        serializer = SampleSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            Sample.objects.create(sampleNumber=request.data["sampleNumber"],sampleVolume=request.data["sampleVolume"], depth = request.data["depth"], sampleLabel = request.data["sampleLabel"], sampleStation = request.data["sampleStation"], storage= request.data["storage"], processed = request.data["processed"], extractionKit = request.data["extractionKit"])

            return Response("Data is inserted successfully", status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
     


def sample_detail(request, sample_id):
    sample_object = SeawaterSample.objects.get(id=sample_id)
    my_sample = {
        'sampleNumber': sample_object.sampleNumber,
        'depth': sample_object.depth,
        'sampleLabel': sample_object.sampleLabel,
        'sampleStation': sample_object.sampleStation
    }

    return JsonResponse(my_sample)
