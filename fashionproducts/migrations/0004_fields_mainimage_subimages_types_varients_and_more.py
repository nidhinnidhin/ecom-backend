# Generated by Django 4.2.9 on 2024-01-18 17:14

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fashionproducts', '0003_color_hex_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mainImage', models.ImageField(default='default_image.png', upload_to='images/')),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='SubImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default_image.png', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fields', models.ManyToManyField(to='fashionproducts.fields')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='fashionproducts.mainimage')),
            ],
        ),
        migrations.CreateModel(
            name='Varients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('types', models.ManyToManyField(to='fashionproducts.types')),
            ],
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='author',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='price',
        ),
        migrations.RemoveField(
            model_name='fashionproductlist',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AddField(
            model_name='mainimage',
            name='subImages',
            field=models.ManyToManyField(to='fashionproducts.subimages'),
        ),
        migrations.AddField(
            model_name='fashionproductlist',
            name='varients',
            field=models.ManyToManyField(to='fashionproducts.varients'),
        ),
    ]
