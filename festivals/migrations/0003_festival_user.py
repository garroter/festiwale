# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 18:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('festivals', '0002_festival_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
            preserve_default=False,
        ),
    ]
