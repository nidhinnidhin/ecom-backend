# Generated by Django 4.1 on 2024-01-08 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_title_product_name_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]