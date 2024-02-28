from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path("cart-checkout/", views.CartCheckoutView.as_view(), name = "cart-checkout"),
    path("test-checkout/", views.TestCheckout.as_view(), name="test-checkout"),
    path("checkout-list/", views.CartCheckoutList.as_view(), name = "checkout-list"),
    path("address-save/", views.AddressSaveView.as_view(), name = "address-save"),
    path("invoice-datas/", views.Sample, name="invoice-data")
]