# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 19:33
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festiwals', '0004_auto_20170220_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='status',
            field=models.BooleanField(default=1, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='festiwal',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Opis'),
        ),
    ]