# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producte', '0007_auto_20170509_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producte',
            name='oferta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oferta.Oferta'),
        ),
    ]
