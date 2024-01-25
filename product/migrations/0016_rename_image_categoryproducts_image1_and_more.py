# Generated by Django 4.2.9 on 2024-01-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_categoryproducts_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryproducts',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='image2',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='image3',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='image4',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='image5',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
    ]
