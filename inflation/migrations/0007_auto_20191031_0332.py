# Generated by Django 2.0 on 2019-10-31 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0003_financialyear_inflation'),
        ('inflation', '0006_auto_20190907_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inflation',
            name='year',
        ),
        migrations.AddField(
            model_name='inflation',
            name='financial_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inflation_f_year', to='dates.FinancialYear'),
        ),
    ]
