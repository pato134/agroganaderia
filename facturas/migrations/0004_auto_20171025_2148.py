# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-25 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0003_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]