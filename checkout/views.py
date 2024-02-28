from cart.models import Cart
from . serializers import CheckoutSerializer
from fashionproducts.models import FashionProductList
from address.models import Address
from . permissions import AdminOnly,OwnerOnly
from rest_framework import permissions,generics,response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.shortcuts import render
from decimal import Decimal

import stripe

class CartCheckoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        Cart.objects.filter(buyer=user, checked_out=False).update(checked_out=True)
        latest_checkout_datetime = Cart.objects.filter(buyer=user, checked_out=True).latest('created_on').created_on
    
        latest_cart_items = Cart.objects.filter(buyer=user, checked_out=True, created_on=latest_checkout_datetime)
        
        invoice_data, total_price, invoice_address = self.get_invoice_data(latest_cart_items)
        
        if user.email:
            subject = 'Thank you for your purchase! Your invoice from Click Shop'
            html_message = render_to_string('invoice_template.html', {'invoice_data': invoice_data, 'total_price': total_price, 'invoice_address': invoice_address})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, 'nidhinbabu171@gmail.com', [user.email], html_message=html_message)
        
        return JsonResponse({"status": "Success"})

    def get_invoice_data(self, cart_items):
        invoice_data = []
        invoice_address = []
        tax = 0
        discount = 0
        shipping_cost = 0
        total_price = Decimal('0')

        for item in cart_items:
            image_url = None
            type = item.types
            main_image = type.images
            image_url = main_image.mainImage.url
            name = item.varient.name
            quantity = item.count
            price = quantity * item.varient.price
            tax += (price * 2) / 100
            discount += (price * 5) / 100
            shipping_cost += price / 20
            total_price += price + tax - discount + shipping_cost

            address_data = {
                'fullname': item.address.fullName,
                'mobile': item.address.mobile,
                'addressline1': item.address.addressLine1,
                'addressline2': item.address.addressLine2,
                'landmark': item.address.landmark,
                'pincode': item.address.pincode,
                'townorcity': item.address.townOrCity,
                'state': item.address.state
            }

            product_data = {
                'image': image_url,
                'name': name,
                'price': price,
                'quantity': quantity
            }

            invoice_data.append(product_data)
            invoice_address.append(address_data)

        return invoice_data, total_price, invoice_address


class AddressSaveView(APIView):
    def post(self, request):
        user = request.user
        address_data = request.data.get("address_data")
        print(address_data)
        address = Address.objects.create(
            buyer = user,
            fullName = address_data["fullName"],
            mobile = address_data["mobile"],
            addressLine1 = address_data["addressLine1"],
            addressLine2 = address_data["addressLine2"],
            landmark = address_data["landmark"],
            pincode = address_data["pincode"],
            townOrCity = address_data["townOrCity"],
            state = address_data["state"],
        )
        cart_checkouts = Cart.objects.filter(buyer = user, checked_out = False)
        cart_checkouts.update(address = address)

        return JsonResponse({'message': 'Address saved successfully'})

    permission_classes = [permissions.IsAuthenticated]


class CartCheckoutList(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user

        checkouts = Cart.objects.filter(buyer=user, checked_out=True)              
        return checkouts

    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]
        

class TestCheckout(APIView):
    def get(self, request, format=None):
        print("Reached")
        stripe.api_key = 'sk_test_51LVzIiSHbelfXOXs1ho3iSSJYxD0r1uV1xJZQyz5z0ocBITBnaESKU0BUirvrqMsbruMAdCj424PaxU9iLPbOiOR002N9N1z9a'

        allProducts = Cart.objects.filter( buyer =  request.user, checked_out = False)
        total = 0
        tax = 0
        discount = 0
        shipping_cost = 0
        grand_total = 0

        for i in allProducts:
            total += i.varient.price * i.count
            tax += (total * 2) / 100
            discount += (total * 5) / 100
            shipping_cost += total / 20
            grand_total += total + tax - discount + shipping_cost

        print(grand_total)
        
        intent = stripe.PaymentIntent.create(
            amount = round(grand_total*100),
            currency = 'inr',
            metadata = {'userid' : request.user.id}
        )
        return JsonResponse({'client_secret': intent.client_secret})



def Sample(request):
    cart = Cart.objects.filter(checked_out=True)
    invoice_data = []
    total_price = Decimal('0')
    tax = 0
    discount = 0
    shipping_cost = 0
    total_price = Decimal('0')
    for item in cart:
        image_url = None
        type = item.types
        main_image = type.images
        image_url = main_image.mainImage.url
        name = item.varient.name
        quantity = item.count
        price = quantity * item.varient.price
        tax = (price * 2) / 100
        discount = (price * 5) / 100
        shipping_cost = price / 20
        total_price = price + tax - discount + shipping_cost
        product_data = {
            'image': image_url,
            'name': name,
            'price': price,
            'quantity': quantity
        }
        invoice_data.append(product_data)
    print(invoice_data)
    return render(request, 'invoice_template.html', context={'invoice_data':invoice_data, 'total_price': total_price})
    
    




