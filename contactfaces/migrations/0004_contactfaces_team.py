# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-08 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactfaces', '0003_auto_20180811_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactfaces',
            name='team',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0),
        ),
    ]