from rest_framework import serializers
from .models import Cart
from fashionproducts.serializers import FashionProductListSerializer


class AddCartSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        varient_id = validated_data.get("varient")
        type_id = validated_data.get("types")
        request = self.context.get('request')
        print("Result",type(varient_id))
        print("Result",type(type_id))
        print("Result",validated_data["product"])
        if Cart.objects.filter(buyer = request.user, product = validated_data["product"],checked_out = False, varient = varient_id, types = type_id).exists():
            cart = Cart.objects.get(buyer = request.user, product = validated_data["product"],
            varient = varient_id,
            types = type_id,
            checked_out = False)
            cart.count = cart.count+1
            cart.save()

        else:
            cart = Cart.objects.create(
                buyer = request.user,
                product = validated_data["product"],
                types = type_id,
                varient = varient_id,
                count = 1
            )
        return cart
    
    class Meta:
        product = FashionProductListSerializer(read_only=True, many=True)
        model = Cart
        fields = ["product","count","checked_out","varient", "types"]

class CartListSerializer(serializers.ModelSerializer):
    def list(self, validated_data):
        request = self.context.get('request')
        cart = Cart.objects.filter(buyer = request.user, checked_out = False )
        return cart

    class Meta:
        model = Cart
        fields = ['id', "product", "varient", "types", "count","checked_out"]
        depth = 5

class CartCheckoutListSerializer(serializers.ModelSerializer):
    def list(self, validated_data):
        request = self.context.get('request')
        cart = Cart.objects.filter(buyer = request.user, checked_out = True )
        return cart

    class Meta:
        model = Cart
        fields = ['id', "product", "varient", "types", "count","checked_out", "delivery_status"]
        depth = 5



class CartDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ["checked_out", "buyer"]

class CartAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


