# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-10 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='sex',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
