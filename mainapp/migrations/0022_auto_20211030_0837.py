# Generated by Django 3.2.8 on 2021-10-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20211029_1800'),
        ('mainapp', '0021_alter_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], default='self', max_length=255, verbose_name='Вид покупки'),
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='cart.OrderItem', verbose_name='Продукты'),
        ),
    ]
