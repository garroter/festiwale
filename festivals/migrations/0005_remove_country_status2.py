# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0004_country_status2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='status2',
        ),
    ]
