from django.urls import path, include
from . import views

app_name = 'bestproduct'

urlpatterns = [
    path('', views.BestProductView.as_view(), name='bestproduct'),
    path('bestproductlist/', views.BestProductListView.as_view(), name='bestproductlist'),
    path('bestproductdetail/<str:pk>/', views.BestProductListDetailView.as_view(), name='product_detail'),
]