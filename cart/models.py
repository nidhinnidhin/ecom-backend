from django.db import models
from fashionproducts.models import FashionProductList
from django.contrib.auth.models import User
from fashionproducts.models import Varients, Types


class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(FashionProductList, on_delete = models.CASCADE)
    varient = models.ForeignKey(Varients,related_name="varient" ,on_delete = models.CASCADE, blank=True, null=True)
    types = models.ForeignKey(Types, related_name = "types" ,on_delete = models.CASCADE, blank=True, null=True)
    count = models.IntegerField(default = 1)
    checked_out = models.BooleanField(default = False, null=True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return f"{self.buyer.username} --> {self.product.name[:50]}"
