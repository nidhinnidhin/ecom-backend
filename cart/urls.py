from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.AddToCartView.as_view(), name = "add-to-cart"),
    path('cartlist/', views.CartListView.as_view(), name = "cart-list"),
    path('cart-count-update/', views.CartCountUpdateView.as_view(), name = "cart-count-update"),
    path('cartdelete/<int:pk>/', views.CartDeleteView.as_view(), name = "cart-delete"),
]