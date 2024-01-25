from django.shortcuts import render
from . models import BankDiscount, ProductDiscounts
from rest_framework.permissions import AllowAny
from rest_framework import generics
from . serializers import BankDiscountSerializer, ProductDiscountSerializer


class BankDiscountView(generics.ListCreateAPIView):
    queryset = BankDiscount.objects.all()
    serializer_class = BankDiscountSerializer
    permission_classes = [AllowAny]

class ProductDiscountView(generics.ListCreateAPIView):
    queryset = ProductDiscounts.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes = [AllowAny]