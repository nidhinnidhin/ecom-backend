# Generated by Django 4.2.9 on 2024-01-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_category_slug'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='FashionProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_image.png', upload_to='images/')),
                ('name', models.CharField(max_length=225)),
                ('discount', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': 'fashionproducts',
            },
        ),
        migrations.CreateModel(
            name='TopProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_image.png', upload_to='images/')),
                ('name', models.CharField(max_length=225)),
                ('discount', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': 'topproducts',
            },
        ),
    ]