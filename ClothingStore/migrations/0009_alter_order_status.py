# Generated by Django 5.0.6 on 2024-07-21 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClothingStore', '0008_alter_order_status_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('on_the_way', 'On the Way'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('return_requested', 'Return Requested'), ('return_received', 'Return Received'), ('refund_issued', 'Refund Issued')], default='ordered', max_length=20),
        ),
    ]
