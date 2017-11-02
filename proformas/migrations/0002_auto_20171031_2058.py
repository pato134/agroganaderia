# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-31 20:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20171025_2148'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proformas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
        migrations.RemoveField(
            model_name='proforma',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='proforma',
            name='tipo_proformas',
        ),
        migrations.AddField(
            model_name='proforma',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proforma',
            name='iva',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='proforma',
            name='numero',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='proforma',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='proforma',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='detalleproforma',
            name='proforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proformas.Proforma'),
        ),
    ]