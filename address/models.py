from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    buyer = models.ForeignKey(User, on_delete =  models.CASCADE)
    fullName = models.CharField(max_length=225)
    mobile = models.CharField(max_length=225)
    addressLine1 = models.CharField(max_length=225)
    addressLine2 = models.CharField(max_length=225)
    landmark = models.CharField(max_length=225)
    pincode = models.CharField(max_length=225)
    townOrCity = models.CharField(max_length=225)
    state = models.CharField(max_length=225)

    def __str__(self):
        return self.buyer.username

