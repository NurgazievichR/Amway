# Generated by Django 4.2.1 on 2023-06-21 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_main_product_orderitem_main_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='product',
            new_name='products',
        ),
    ]
