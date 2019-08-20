# Generated by Django 2.0 on 2019-08-20 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seasonality', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productseasonality',
            options={'verbose_name': 'Product Seasonality', 'verbose_name_plural': 'Product Seasonalities'},
        ),
        migrations.RenameField(
            model_name='productseasonality',
            old_name='month_10_seasonality',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='productseasonality',
            old_name='seasonality_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_11_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_12_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_1_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_2_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_3_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_4_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_5_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_6_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_7_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_8_seasonality',
        ),
        migrations.RemoveField(
            model_name='productseasonality',
            name='month_9_seasonality',
        ),
        migrations.AddField(
            model_name='productseasonality',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productseasonality',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='productseasonality',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
