from django.urls import path, include
from . import views

app_name = 'bankdiscount'

urlpatterns = [
    path('', views.BankDiscountView.as_view(), name='slider'),
    path('productdiscount/', views.ProductDiscountView.as_view(), name='productdiscount'),
]