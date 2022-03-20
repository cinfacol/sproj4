# Generated by Django 4.0 on 2022-03-20 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('store', '0001_initial'),
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.post'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_addresss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='perfiles.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_addresss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='perfiles.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfiles.userbase', verbose_name='order_user'),
        ),
    ]
