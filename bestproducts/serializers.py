from rest_framework import serializers
from . models import BestProducts,  BestProductList



class BestProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestProducts
        fields = "__all__"

class BestProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestProductList
        fields = "__all__"

class BestProductListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestProductList
        fields = "__all__"