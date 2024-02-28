from django.shortcuts import render
from . serializers import AddressSerializer, AddressListSerializer
from . models import Address
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressEditView(APIView):
    def put(self, request):
        user = get_object_or_404(Address, buyer = request.user)
        user.fullName = request.data["fullName"]
        user.mobile = request.data["mobile"]
        user.addressLine1 = request.data["addressLine1"]
        user.addressLine2 = request.data["addressLine2"]
        user.landmark = request.data["landmark"]
        user.pincode = request.data["pincode"]
        user.townOrCity = request.data["townOrCity"]
        user.state = request.data["state"]

        user.save()
        return Response({"status": "Edited Successfully"})
    permission_classes = [permissions.IsAuthenticated]


class AddressDetailView(APIView):
    def get(self, request):
        if Address.objects.filter(buyer = request.user).exists():
            user = Address.objects.filter(buyer = request.user).order_by("id").last()
            data = {
                "fullName": user.fullName,
                "mobile": user.mobile,
                "addressLine1": user.addressLine1,
                "addressLine2": user.addressLine2,
                "landmark": user.landmark,
                "pincode": user.pincode,
                "townOrCity": user.townOrCity,
                "state": user.state
            }
        else:
            data = {
                "fullName": "",
                "mobile": "",
                "addressLine1": "",
                "addressLine2": "",
                "landmark": "",
                "pincode": "",
                "townOrCity": "",
                "state": ""
            }
        return Response(data)
    parser_classes = [permissions.IsAuthenticated]
