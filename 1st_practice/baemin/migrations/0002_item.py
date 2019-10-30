# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-16 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baemin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baemin.Shop')),
            ],
        ),
    ]
