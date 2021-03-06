# Generated by Django 2.0 on 2019-09-07 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rampup', '0002_auto_20190907_1301'),
        ('products', '0001_initial'),
        ('seasonality', '0003_auto_20190907_1301'),
        ('revenues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRevenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inflation', models.FloatField(default=1)),
                ('product_revenue', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revenue_product', to='products.Product')),
                ('product_rampup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revenue_product_rampup', to='rampup.ProductRampUp')),
                ('product_seasonality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revenue_product_seasonality', to='seasonality.ProductSeasonality')),
            ],
            options={
                'verbose_name': 'Product Revenue',
                'verbose_name_plural': 'Products Revenue',
            },
        ),
        migrations.RemoveField(
            model_name='revenue',
            name='product',
        ),
        migrations.RemoveField(
            model_name='revenue',
            name='seasonality',
        ),
        migrations.DeleteModel(
            name='Revenue',
        ),
    ]
