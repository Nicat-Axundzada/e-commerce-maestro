# Generated by Django 5.0.3 on 2024-05-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_rename_product_id_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processing', 'Hazırlanır'), ('Delivered', 'Təslim edildi'), ('Cancelled', 'Ləğv edildi')], default='Processing', max_length=20),
        ),
    ]
