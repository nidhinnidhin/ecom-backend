# Generated by Django 4.2.9 on 2024-01-18 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashionproducts', '0005_rename_image_subimages_image1_subimages_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subimages',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='subimages',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='subimages',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='subimages',
            name='image4',
        ),
    ]
