from rest_framework import serializers
from . models import FashionProducts, FashionProductList

class FashionProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionProducts
        fields = "__all__"
    
class FashionProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionProductList
        fields = "__all__"
        depth = 4

class FashionProductListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionProductList
        fields = "__all__"
        depth = 4