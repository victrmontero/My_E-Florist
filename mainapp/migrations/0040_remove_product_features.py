# Generated by Django 3.2.8 on 2022-01-25 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_auto_20211126_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='features',
        ),
    ]
