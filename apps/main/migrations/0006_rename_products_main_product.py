# Generated by Django 4.2.1 on 2023-06-21 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_product_main_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='products',
            new_name='product',
        ),
    ]
