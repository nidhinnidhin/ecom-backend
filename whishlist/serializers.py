from rest_framework import serializers
from .models import Whishlist
from fashionproducts.serializers import FashionProductListSerializer

class AddWhishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whishlist
        fields = ['id', 'product', 'varient', 'types']