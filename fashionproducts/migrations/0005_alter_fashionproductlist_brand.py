# Generated by Django 5.0.1 on 2024-02-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionproducts', '0004_fashionproductlist_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashionproductlist',
            name='brand',
            field=models.CharField(default='Addidas', max_length=225),
        ),
    ]
