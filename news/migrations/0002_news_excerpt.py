# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='excerpt',
            field=models.TextField(default=1, verbose_name='Krótki opis'),
            preserve_default=False,
        ),
    ]
