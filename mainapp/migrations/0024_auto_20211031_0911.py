# Generated by Django 3.2.8 on 2021-10-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20211030_1115'),
        ('mainapp', '0023_auto_20211030_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='products_cart',
        ),
        migrations.AddField(
            model_name='order',
            name='products_wishlist',
            field=models.ManyToManyField(to='wishlist.OrderItem', verbose_name='Продукты'),
        ),
    ]
