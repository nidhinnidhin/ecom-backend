# Generated by Django 4.2.9 on 2024-01-25 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fashionproducts', '0006_rename_image1_subimages_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashionproducts.fashionproductlist')),
                ('types', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fashionproducts.types')),
                ('varient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fashionproducts.varients')),
            ],
        ),
    ]
