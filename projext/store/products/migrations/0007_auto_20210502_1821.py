# Generated by Django 3.2 on 2021-05-02 12:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productsupload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Buyer/image'),
        ),
        migrations.AlterField(
            model_name='productsupload',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Seller/image'),
        ),
    ]