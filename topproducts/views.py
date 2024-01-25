from django.shortcuts import render
from . serializers import TopProductSerializer,TopProductListDetailSerializer, TopProductListSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . models import TopProducts, TopProductList


class TopProductView(generics.ListCreateAPIView):
    queryset = TopProducts.objects.all()
    serializer_class = TopProductSerializer
    permission_classes = [AllowAny]

class TopProductListView(generics.ListCreateAPIView):
    queryset = TopProductList.objects.all()
    serializer_class = TopProductListSerializer
    permission_classes = [AllowAny]

class TopProductListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TopProductList.objects.all()
    serializer_class = TopProductListDetailSerializer
    permission_classes = [AllowAny]