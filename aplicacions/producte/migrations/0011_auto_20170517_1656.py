# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producte', '0010_auto_20170517_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producte',
            name='imatge',
            field=models.ImageField(blank=True, null=True, upload_to=b'img'),
        ),
    ]