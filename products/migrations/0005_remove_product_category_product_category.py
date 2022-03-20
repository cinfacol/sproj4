# Generated by Django 4.0 on 2022-03-20 02:53

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeManyToManyField(to='products.Category'),
        ),
    ]