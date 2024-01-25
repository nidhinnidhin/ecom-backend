from django.db import models
from django.contrib.auth.models import User
from fashionproducts.models import Varients, Types
from fashionproducts.models import FashionProductList

class Whishlist(models.Model):
    buyer = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(FashionProductList, on_delete = models.CASCADE)
    varient = models.ForeignKey(Varients, on_delete = models.CASCADE, blank = True, null = True)
    types = models.ForeignKey(Types, on_delete = models.CASCADE, blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.buyer.username