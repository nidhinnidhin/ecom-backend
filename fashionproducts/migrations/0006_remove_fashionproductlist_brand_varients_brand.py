# Generated by Django 5.0.1 on 2024-02-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionproducts', '0005_alter_fashionproductlist_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='brand',
        ),
        migrations.AddField(
            model_name='varients',
            name='brand',
            field=models.CharField(max_length=225, null=True),
        ),
    ]