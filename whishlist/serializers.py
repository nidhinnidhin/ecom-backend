from rest_framework import serializers
from .models import Whishlist
from fashionproducts.serializers import FashionProductListSerializer

class AddWhishlistSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_data = validated_data.get("product")
        varient_id = validated_data.get("varient")
        type_id = validated_data.get("types")
        request = self.context.get("request")
        
        if not product_data:
            raise serializers.ValidationError("Product data is required.")

        product_id = product_data.id

        existing_wishlist = Whishlist.objects.filter(
            buyer=request.user,
            product_id=product_id,
            varient=varient_id,
            types=type_id
        )
        if existing_wishlist.exists():
            raise serializers.ValidationError("This product is already in the wishlist.")

        whishlist = Whishlist.objects.create(
            buyer=request.user,
            product=product_data,
            types=type_id,
            varient=varient_id
        )
        return whishlist

    class Meta:
        product = FashionProductListSerializer(read_only=True)
        model = Whishlist
        fields = ['product', 'varient', 'types']

class WhishlistSerializer(serializers.ModelSerializer):
    def list(self,validated_data):
        request = self.context.get('request')
        if(Whishlist.objects.filter(buyer = request.user, product = validated_data['product'])):
            whishlist = Whishlist.objects.filter(buyer = request.user, product = validated_data["product"])
            return whishlist
    class Meta:
        model = Whishlist
        fields = ['id','product','varient','types']
        depth = 5

class WhishlistDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whishlist
        fields = "__all__"