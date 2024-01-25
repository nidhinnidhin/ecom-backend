from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('api/products/category/<int:category_id>/', views.ProductListByCategoryAPIView.as_view(), name='product-list-by-category'),
    path('api/products/category/detail/<int:pk>', views.CategoryProductDetailView.as_view(), name='category-products-detail'),
    path('api/products/category/list', views.CategoryProductDetailListView.as_view(), name='category-products-detail-list'),
    
]