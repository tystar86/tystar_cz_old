# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0006_auto_20170903_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]