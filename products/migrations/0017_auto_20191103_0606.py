# Generated by Django 2.0 on 2019-11-03 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0003_financialyear_inflation'),
        ('products', '0016_auto_20191103_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax',
            name='profit_before_tax',
        ),
        migrations.AddField(
            model_name='tax',
            name='financial_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tax_f_year', to='dates.FinancialYear'),
        ),
    ]
