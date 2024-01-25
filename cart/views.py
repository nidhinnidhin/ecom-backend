from django.shortcuts import render
from rest_framework import generics, permissions, views
from rest_framework.response import Response
from .models import Cart
from. serializers import AddCartSerializer, CartAdminSerializer, CartListSerializer, CartDeleteSerializer
from .permissions import OwnerOrAdmin
from rest_framework import status
# from fashionproducts.models import FashionProductList


class AddToCartView(generics.ListCreateAPIView):

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            carts = Cart.objects.all()
        
        else:
            carts = Cart.objects.filter(buyer = user, checked_out = False)
        
        return carts

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return CartAdminSerializer
        
        return AddCartSerializer 

    permission_classes = [permissions.IsAuthenticated]

class CartListView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            carts = Cart.objects.all()
        
        else:
            carts = Cart.objects.filter(buyer = user, checked_out = False)
        
        return carts

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return CartAdminSerializer
        
        return CartListSerializer 

    permission_classes = [permissions.IsAuthenticated]
    

class CartCountUpdateView(views.APIView):
    def post(self, request, *args, **kwargs):
        cart_id = request.data.get('cart_id')
        print("=====================================")
        print(cart_id)
        is_increment = request.data.get('is_increment')
        try:
            cart_instance = Cart.objects.get(id=cart_id)
            print("cart", cart_instance)
            print("user", request.user)
            print("=====================================")
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if is_increment:
            cart_instance.count += 1
            cart_instance.save()
        else:
            if cart_instance.count > 1:
                cart_instance.count -= 1
                cart_instance.save()
            else:
                cart_instance.delete()

        return Response({'message': 'success'}, status=status.HTTP_200_OK)

class CartDeleteView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]
