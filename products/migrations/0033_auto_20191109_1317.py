# Generated by Django 2.0 on 2019-11-09 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20191109_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='financial_year',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='month',
        ),
    ]
