# Generated by Django 4.0 on 2022-03-27 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='products.product'),
        ),
    ]