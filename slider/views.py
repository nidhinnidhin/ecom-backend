from django.shortcuts import render
from . models import Slider
from rest_framework.permissions import AllowAny
from rest_framework import generics
from . serializers import SliderSerializer


class SliderView(generics.ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [AllowAny]

