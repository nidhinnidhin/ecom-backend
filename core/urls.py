from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls', namespace='store')),
    path('fashionproduct/', include('fashionproducts.urls', namespace='fashionproducts')),
    path('slider/', include('slider.urls', namespace='slider')),
    path('bankdiscount/', include('bankdiscount.urls', namespace='bankdiscount')),
    path('account/', include('user.urls', namespace ="user")),
    path('cart/', include('cart.urls', namespace ="cart")),
    path('address/', include('address.urls', namespace ="address")),
    path('whishlist/', include('whishlist.urls', namespace ="whishlist")),
    path('checkout/', include('checkout.urls', namespace ="checkout")),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": settings.STATIC_ROOT}),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
