# Generated by Django 2.0 on 2019-11-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rampup', '0006_auto_20191108_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productrampup',
            old_name='percentage',
            new_name='demand_percentage',
        ),
        migrations.AddField(
            model_name='productrampup',
            name='demand_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
