from rest_framework import serializers
from . models import CategoryProducts, Category


class CategoryListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProducts
        fields = '__all__'

class CategoryProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProducts
        fields = '__all__'


