# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_weather', '0002_auto_20180514_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='temperature',
            field=models.FloatField(default=0),
        ),
    ]
