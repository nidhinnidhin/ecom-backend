from django.urls import path, include
from . import views

app_name = 'topproduct'

urlpatterns = [
    path('', views.TopProductView.as_view(), name='topproducts'),
    path('topproductlist/', views.TopProductListView.as_view(), name='toptproductlist'),
    path('topproductdetail/<str:pk>/', views.TopProductListDetailView.as_view(), name='topproduct_detail'),
]