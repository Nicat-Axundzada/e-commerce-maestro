# Generated by Django 5.0.3 on 2024-05-08 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_number_of_products_alter_product_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='number_of_products',
            new_name='stock',
        ),
    ]
