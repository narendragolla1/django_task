# Generated by Django 4.2.2 on 2023-06-10 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
    ]
