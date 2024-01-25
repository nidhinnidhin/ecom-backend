from django.shortcuts import render
from . serializers import FashionProductSerializer, FashionProductListSerializer,FashionProductListDetailSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . models import FashionProducts, FashionProductList
from rest_framework.filters import SearchFilter, OrderingFilter


class FashionProductView(generics.ListCreateAPIView):
    queryset = FashionProducts.objects.all()
    serializer_class = FashionProductSerializer
    permission_classes = [AllowAny]

class FashionProductListView(generics.ListCreateAPIView):
    queryset = FashionProductList.objects.all()
    serializer_class = FashionProductListSerializer
    permission_classes = [AllowAny]

class FashionProductListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FashionProductList.objects.all()
    serializer_class = FashionProductListDetailSerializer
    permission_classes = [AllowAny]

class ProductFilter(generics.ListAPIView):
    queryset = FashionProductList.objects.all()
    serializer_class = FashionProductListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']