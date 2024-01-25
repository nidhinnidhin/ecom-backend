from rest_framework import serializers
from . models import BankDiscount, ProductDiscounts

class BankDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDiscount
        fields = "__all__"

class ProductDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDiscounts
        fields = "__all__"