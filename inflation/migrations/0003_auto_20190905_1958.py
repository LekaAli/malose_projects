# Generated by Django 2.0 on 2019-09-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflation', '0002_auto_20190820_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inflation',
            name='year',
            field=models.SmallIntegerField(default=2),
        ),
    ]
