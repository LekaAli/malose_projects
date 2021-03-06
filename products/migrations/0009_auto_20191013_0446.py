# Generated by Django 2.0 on 2019-10-13 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20191012_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profitbeforetax',
            old_name='total_value',
            new_name='total_gross_value',
        ),
        migrations.AlterField(
            model_name='product',
            name='financial_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_fin_year', to='dates.FinancialYear'),
        ),
        migrations.AlterField(
            model_name='product',
            name='projection_start',
            field=models.CharField(choices=[('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], max_length=10, null=True),
        ),
    ]
