# Generated by Django 4.1.5 on 2023-01-19 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_manage', '0003_delete_category_delete_order_delete_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
