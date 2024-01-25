from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls', namespace='store')),
    path('bestproduct/', include('bestproducts.urls', namespace='bestproducts')),
    path('topproduct/', include('topproducts.urls', namespace='topproducts')),
    path('fashionproduct/', include('fashionproducts.urls', namespace='fashionproducts')),
    path('slider/', include('slider.urls', namespace='slider')),
    path('bankdiscount/', include('bankdiscount.urls', namespace='bankdiscount')),
    path('account/', include('account.urls', namespace ="account")),
    path('cart/', include('cart.urls', namespace ="cart")),
    path('whishlist/', include('whishlist.urls', namespace ="whishlist")),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
