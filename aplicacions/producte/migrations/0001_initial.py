# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('preu', models.FloatField()),
            ],
        ),
    ]
