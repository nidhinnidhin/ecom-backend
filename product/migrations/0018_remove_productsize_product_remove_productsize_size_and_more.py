# Generated by Django 4.2.9 on 2024-01-16 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_bestproductsize_productsize_bestproductlist_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size',
        ),
        migrations.RemoveField(
            model_name='bestproductlist',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='BestProductSize',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
    ]