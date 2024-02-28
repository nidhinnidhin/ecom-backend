from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='default_image.png')
    discount = models.CharField(max_length=225, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class CategoryProducts(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'product_creator')
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='images/', default='default_image.png')
    image2 = models.ImageField(upload_to='images/', default='default_image.png')
    image3 = models.ImageField(upload_to='images/', default='default_image.png')
    image4 = models.ImageField(upload_to='images/', default='default_image.png')
    image5 = models.ImageField(upload_to='images/', default='default_image.png')
    slug = models.SlugField(max_length=225)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Category-products'
        ordering = ('-created',)

    def __str__(self):
        return self.name
    
