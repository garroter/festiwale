# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festiwals', '0003_auto_20170216_1752'),
        ('news', '0006_auto_20170216_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='festiwals',
            field=models.ManyToManyField(to='festiwals.Festiwal', verbose_name='Festiwale'),
        ),
    ]