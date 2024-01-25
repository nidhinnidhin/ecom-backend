from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BestProducts(models.Model):
    image = models.ImageField(upload_to='images/', default='default_image.png')
    name = models.CharField(max_length=225)
    discount = models.CharField(max_length=225)

    class Meta:
        verbose_name_plural = 'bestproducts'

    def __str__(self):
        return self.name
    
class BestProductList(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='images/', default='default_image.png')
    image2 = models.ImageField(upload_to='images/', default='default_image.png')
    image3 = models.ImageField(upload_to='images/', default='default_image.png')
    image4 = models.ImageField(upload_to='images/', default='default_image.png')
    image5 = models.ImageField(upload_to='images/', default='default_image.png') 
    price = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField(max_length=225, default="products")
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'bestproductslist'

    def __str__(self):
        return self.name