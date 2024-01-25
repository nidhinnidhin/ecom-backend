from rest_framework import serializers
from . models import TopProducts, TopProductList


class TopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProducts
        fields = "__all__"

class TopProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProductList
        fields = "__all__"

class TopProductListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProductList
        fields = "__all__"