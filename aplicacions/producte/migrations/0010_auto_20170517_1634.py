# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producte', '0009_auto_20170509_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='producte',
            name='imatge',
            field=models.ImageField(blank=True, null=True, upload_to=b'static/img/Producte'),
        ),
        migrations.AlterField(
            model_name='producte',
            name='descripcio',
            field=models.CharField(max_length=500, null=True),
        ),
    ]