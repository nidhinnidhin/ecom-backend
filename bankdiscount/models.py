from django.db import models


class BankDiscount(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='default_image.png')

    class Meta:
        verbose_name_plural = 'bankdiscounts'

    def __str__(self):
        return self.name

class ProductDiscounts(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images/', default='default_image.png')

    class Meta:
        verbose_name_plural = 'productdiscounts'

    def __str__(self):
        return self.name
