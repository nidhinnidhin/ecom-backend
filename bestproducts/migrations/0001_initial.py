# Generated by Django 4.2.9 on 2024-01-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(default='admin', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image1', models.ImageField(default='default_image.png', upload_to='images/')),
                ('image2', models.ImageField(default='default_image.png', upload_to='images/')),
                ('image3', models.ImageField(default='default_image.png', upload_to='images/')),
                ('image4', models.ImageField(default='default_image.png', upload_to='images/')),
                ('image5', models.ImageField(default='default_image.png', upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('slug', models.SlugField(default='products', max_length=225)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'bestproductslist',
            },
        ),
        migrations.CreateModel(
            name='BestProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_image.png', upload_to='images/')),
                ('name', models.CharField(max_length=225)),
                ('discount', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': 'bestproducts',
            },
        ),
    ]
