from django.contrib import admin
from . models import BankDiscount, ProductDiscounts


admin.site.register(BankDiscount)
admin.site.register(ProductDiscounts)
