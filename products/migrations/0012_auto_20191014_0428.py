# Generated by Django 2.0 on 2019-10-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20191013_0512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='financial_year',
        ),
        migrations.AlterField(
            model_name='sale',
            name='period',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]