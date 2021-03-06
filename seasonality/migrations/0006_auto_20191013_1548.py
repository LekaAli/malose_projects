# Generated by Django 2.0 on 2019-10-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasonality', '0005_auto_20190907_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productseasonality',
            name='description',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='name',
        ),
        migrations.AlterField(
            model_name='productseasonality',
            name='month',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True),
        ),
    ]
