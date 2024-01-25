from django.shortcuts import render
from .serializers import AddWhishlistSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . models import Whishlist
from rest_framework.response import Response


class AddWhishlistView(generics.ListAPIView):
    serializer_class = AddWhishlistSerializer
    permission_classes = [IsAuthenticated]

    def create(self, validated_data):
        user = self.request.user
        varient_id = validated_data.get["varient"]
        type_id = validated_data.get["types"]
        if user.is_superuser:
            whishlist = Whishlist.objects.all()
        else:
            whishlist = Whishlist.objects.filter(buyer = user, product = validated_data['product'], varient = varient_id, types = type_id)
        return whishlist