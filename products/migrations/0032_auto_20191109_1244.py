# Generated by Django 2.0 on 2019-11-09 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20191109_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostOfSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=75, null=True)),
                ('percentage', models.PositiveSmallIntegerField(default=0, help_text='Cost of sale value should be a percentage')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cost Of Sale',
                'verbose_name_plural': 'Cost Of Sales',
            },
        ),
        migrations.RemoveField(
            model_name='grossprofit',
            name='cost_of_sale_percentage',
        ),
        migrations.AddField(
            model_name='grossprofit',
            name='cost_of_sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cost_of_sale', to='products.CostOfSale'),
        ),
    ]
