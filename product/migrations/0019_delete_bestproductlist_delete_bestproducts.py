# Generated by Django 4.2.9 on 2024-01-16 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_productsize_product_remove_productsize_size_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BestProductList',
        ),
        migrations.DeleteModel(
            name='BestProducts',
        ),
    ]
