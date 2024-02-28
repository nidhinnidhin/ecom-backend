from django.urls import path, include
from . import views

app_name = 'fashionproduct'

urlpatterns = [
    path('', views.FashionProductView.as_view(), name='fashionproducts'),
    path('fashionproductlist/', views.FashionProductListView.as_view(), name='fashiontproductlist'),
    path('fashionproductdetail/<str:pk>/', views.FashionProductListDetailView.as_view(), name='fashionproduct_detail'),
    path('search/', views.ProductFilter.as_view(), name = "product-filter"),
    path('api/product/category/<int:category_id>/', views.ProductListByCategoryAPIView.as_view(), name='product-list-by-category'),
    path('product-search/', views.ProductSearchView.as_view(), name='product_search'),
    
]