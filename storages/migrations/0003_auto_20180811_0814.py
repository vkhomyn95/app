# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-11 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storages', '0002_auto_20180811_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]