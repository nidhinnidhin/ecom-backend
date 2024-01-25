from django.urls import path, include
from . import views

app_name = 'slider'

urlpatterns = [
    path('', views.SliderView.as_view(), name='slider'),
]