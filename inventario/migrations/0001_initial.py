# Generated by Django 3.2.9 on 2021-12-07 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(help_text='format: required, unique, max-20', max_length=20, unique=True, verbose_name='stock keeping unit')),
                ('upc', models.CharField(help_text='format: required, unique, max-12', max_length=12, unique=True, verbose_name='universal product code')),
                ('is_active', models.BooleanField(default=True, help_text='format: true=product visible', verbose_name='product visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='date sub-product created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='date sub-product updated')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_checked', models.DateTimeField(blank=True, help_text='format: Y-m-d H:M:S, null-true, blank-true', null=True, verbose_name='inventory stock check date')),
                ('units', models.IntegerField(default=0, help_text='format: required, default-0', verbose_name='units/qty of stock')),
                ('units_sold', models.IntegerField(default=0, help_text='format: required, default-0', verbose_name='units sold to date')),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='product_inventory', to='inventario.inventory')),
            ],
        ),
    ]
