# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-14 15:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storages', '0001_initial'),
        ('place', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('site', models.URLField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.City')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_in', to=settings.AUTH_USER_MODEL)),
                ('sellers', models.ManyToManyField(related_name='seller_in', to=settings.AUTH_USER_MODEL)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storages.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='type_of_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.TypeOfStore'),
        ),
    ]
