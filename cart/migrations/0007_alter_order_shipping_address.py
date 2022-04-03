# Generated by Django 4.0 on 2022-04-03 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_alter_address_options_alter_address_oficina_address_and_more'),
        ('cart', '0006_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirección_de_envío', to='perfiles.address'),
        ),
    ]
