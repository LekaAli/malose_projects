# Generated by Django 2.0 on 2019-11-11 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasonality', '0008_auto_20191108_2122'),
        ('rampup', '0007_auto_20191108_2131'),
        ('products', '0035_auto_20191110_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSeasonalityRampUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_link', to='products.Product')),
                ('rampup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rampup_link', to='rampup.ProductRampUp')),
                ('seasonality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seasonality_link', to='seasonality.ProductSeasonality')),
            ],
            options={
                'verbose_name': 'Product Seasonality Ramp Up Link',
                'verbose_name_plural': 'Product Seasonality Ramp Up Links',
            },
        ),
    ]
