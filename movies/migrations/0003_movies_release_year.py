# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-01 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movies_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='release_year',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]