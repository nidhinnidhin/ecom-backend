# Generated by Django 4.2.9 on 2024-01-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankdiscount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDiscounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('image', models.ImageField(default='default_image.png', upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'productdiscounts',
            },
        ),
    ]
