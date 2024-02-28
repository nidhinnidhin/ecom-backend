from django.shortcuts import render
from .serializers import AddWhishlistSerializer,WhishlistSerializer,WhishlistDeleteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . models import Whishlist
from rest_framework.response import Response


class AddWhishlistView(generics.ListCreateAPIView):
    queryset = Whishlist.objects.all()
    serializer_class = AddWhishlistSerializer
    permission_classes = [IsAuthenticated]

class WhishlistView(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            whishlist = Whishlist.objects.all().order_by('-created_on')
        
        else:
            whishlist = Whishlist.objects.filter(buyer = user).order_by('-created_on')
        
        return whishlist
    serializer_class = WhishlistSerializer
    permission_classes = [IsAuthenticated]

class WhishlistDeleteView(generics.DestroyAPIView):
    queryset = Whishlist.objects.all()
    serializer_class = WhishlistDeleteSerializer
    permission_classes = [IsAuthenticated]