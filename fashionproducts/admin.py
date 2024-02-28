from .models import FashionProducts, FashionProductList,SubImages, MainImage, Fields, Types, Varients
from django.contrib import admin

admin.site.register(SubImages)
admin.site.register(MainImage)
admin.site.register(Fields)
admin.site.register(Types)
admin.site.register(Varients)
admin.site.register(FashionProducts)
admin.site.register(FashionProductList)