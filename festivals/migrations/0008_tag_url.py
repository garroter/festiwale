# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0007_artist_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='url',
            field=models.SlugField(blank=True, verbose_name='url'),
        ),
    ]
