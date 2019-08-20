# Generated by Django 2.0 on 2019-08-20 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sale'),
        ('seasonality', '0002_auto_20190820_0411'),
        ('revenues', '0002_auto_20190820_0411'),
        ('inflation', '0002_auto_20190820_0411'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='sale',
            name='inflation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_inflation', to='inflation.Inflation'),
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_price', to='products.Product'),
        ),
        migrations.AddField(
            model_name='sale',
            name='seasonality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_seasonality', to='seasonality.ProductSeasonality'),
        ),
    ]
