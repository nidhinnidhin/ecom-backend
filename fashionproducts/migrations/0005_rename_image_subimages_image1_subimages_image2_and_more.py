# Generated by Django 4.2.9 on 2024-01-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionproducts', '0004_fields_mainimage_subimages_types_varients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subimages',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='subimages',
            name='image2',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='subimages',
            name='image3',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='subimages',
            name='image4',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
    ]
