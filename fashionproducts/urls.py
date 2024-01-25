from django.urls import path, include
from . import views

app_name = 'fashionproduct'

urlpatterns = [
    path('', views.FashionProductView.as_view(), name='fashionproducts'),
    path('fashionproductlist/', views.FashionProductListView.as_view(), name='fashiontproductlist'),
    path('fashionproductdetail/<str:pk>/', views.FashionProductListDetailView.as_view(), name='fashionproduct_detail'),
    path('search/', views.ProductFilter.as_view(), name = "product-filter"),
]