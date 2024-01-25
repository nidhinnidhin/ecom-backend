from django.urls import path
from . import views

app_name = "whishlist"

urlpatterns = [
    path('', views.AddWhishlistView.as_view(), name = "add-to-whishlist"),
]
