# Generated by Django 3.2 on 2021-04-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productsupload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsupload',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/media/'),
        ),
    ]
