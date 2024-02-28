from django.urls import path
from . import views

app_name = "whishlist"

urlpatterns = [
    path('', views.AddWhishlistView.as_view(), name = "add-to-whishlist"),
    path('whishlist/', views.WhishlistView.as_view(), name = "whishlist"),
    path('delete-wishlist/<int:pk>/', views.WhishlistDeleteView.as_view(), name = "delete-wishlist"),
]
