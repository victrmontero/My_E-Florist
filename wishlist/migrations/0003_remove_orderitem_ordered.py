# Generated by Django 3.2.8 on 2021-11-02 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20211030_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
    ]
