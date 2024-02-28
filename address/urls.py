from . import views
from django.urls import path, include

app_name = 'address'

urlpatterns = [
    path('', views.AddressView.as_view(), name='address'),
    path('address-list/', views.AddressListView.as_view(), name="address-list"),
    path('address-edit/', views.AddressEditView.as_view(), name="address-edit"),
    path('address-detail/', views.AddressDetailView.as_view(), name="address-detail")
]