from django.shortcuts import render
from . serializers import CategoryListingSerializer, CategoryProducts, CategoryProductSerializer, CategoryProductDetailSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . models import CategoryProducts, Category
from rest_framework.response import Response
from rest_framework.views import APIView

                      
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListingSerializer
    permission_classes = [AllowAny]

class CategoryProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryProducts.objects.all()
    serializer_class = CategoryProductDetailSerializer
    permission_classes = [AllowAny]

class CategoryProductDetailListView(generics.ListCreateAPIView):
    queryset = CategoryProducts.objects.all()
    serializer_class = CategoryProductDetailSerializer
    permission_classes = [AllowAny]

class ProductListByCategoryAPIView(APIView):
    def get(self, request, category_id):
        products = CategoryProducts.objects.filter(category__id=category_id)
        serializer = CategoryProductSerializer(products, many=True)
        return Response(serializer.data)
                      


