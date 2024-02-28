from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get("request")
        address = Address()
    
        address.buyer = request.user
        address.fullName = validated_data["fullName"]
        address.mobile = validated_data["mobile"]
        address.addressLine1 = validated_data["addressLine1"]
        address.addressLine2 = validated_data["addressLine2"]
        address.landmark = validated_data["landmark"]
        address.pincode = validated_data["pincode"]
        address.townOrCity = validated_data["townOrCity"]
        address.state = validated_data["state"]

        address.save()
        return address

    class Meta:
        model = Address
        fields = ["fullName","mobile","addressLine1", "addressLine2", "landmark", "pincode", "townOrCity","state"]


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["fullName","mobile","addressLine1", "addressLine2", "landmark", "pincode", "townOrCity","state"]

