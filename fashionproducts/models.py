from django.db import models
from django.contrib.auth import get_user_model
from colorfield.fields import ColorField
from product.models import Category

User = get_user_model()

class FashionProducts(models.Model):
    image = models.ImageField(upload_to='images/', default='default_image.png')
    name = models.CharField(max_length=225)
    discount = models.CharField(max_length=225)

    class Meta:
        verbose_name_plural = 'fashionproducts'

    def __str__(self):
        return self.name


class SubImages(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='default_image.png') 

    def __str__(self):
        return self.name
    
class MainImage(models.Model):
    name = models.CharField(max_length=100)
    mainImage = models.ImageField(upload_to='images/', default='default_image.png')
    subImages = models.ManyToManyField(SubImages)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name
    
class Fields(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value

class Types(models.Model):
    name = models.CharField(max_length=100)
    fields = models.ManyToManyField(Fields)
    images = models.ForeignKey(MainImage, related_name = 'types', on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
class Varients(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=225, null = True)
    types = models.ManyToManyField(Types)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    def __str__(self):
        return self.name
    
class FashionProductList(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=225, null = True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    varients = models.ManyToManyField(Varients)

    class Meta:
        verbose_name_plural = 'Fashionproductlist'

    def __str__(self):
        return self.name