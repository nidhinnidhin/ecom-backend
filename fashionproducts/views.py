from django.shortcuts import render
from . serializers import FashionProductSerializer, FashionProductListSerializer,FashionProductListDetailSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . models import FashionProducts, FashionProductList
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Cart

class FashionProductView(generics.ListCreateAPIView):
    queryset = FashionProducts.objects.all()
    serializer_class = FashionProductSerializer
    permission_classes = [AllowAny]

class FashionProductListView(generics.ListCreateAPIView):
    queryset = FashionProductList.objects.filter(in_stock = True)
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

class ProductListByCategoryAPIView(APIView):
    def get(self, request, category_id):
        print("ListByCategory")
        products = FashionProductList.objects.filter(category__id=category_id)
        print(products)
        serializer = FashionProductListSerializer(products, many=True)
        return Response(serializer.data)

class ProductSearchView(APIView):
    queryset = FashionProductList.objects.all()
    serializer_class = FashionProductListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']

