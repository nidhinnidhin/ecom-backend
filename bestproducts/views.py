from django.shortcuts import render
from . serializers import BestProductListDetailSerializer, BestProductsSerializer, BestProductListSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . models import BestProducts, BestProductList
from rest_framework.response import Response
from rest_framework.views import APIView




class BestProductView(generics.ListCreateAPIView):
    queryset = BestProducts.objects.all()
    serializer_class = BestProductsSerializer
    permission_classes = [AllowAny]

class BestProductListView(generics.ListCreateAPIView):
    queryset = BestProductList.objects.all()
    serializer_class = BestProductListSerializer
    permission_classes = [AllowAny]

class BestProductListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BestProductList.objects.all()
    serializer_class = BestProductListDetailSerializer
    permission_classes = [AllowAny]