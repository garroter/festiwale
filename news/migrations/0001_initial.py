# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 18:10
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(unique_for_date='pub_date', verbose_name='url')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('pub_date', models.DateTimeField(verbose_name='Data publikacji')),
                ('seo_title', models.CharField(max_length=255, verbose_name='Seo tytuł :)')),
                ('seo_keywords', models.CharField(max_length=255, verbose_name='Seo słowa kluczowe :)')),
                ('seo_description', models.TextField(verbose_name='Seo opis :)')),
                ('status', models.BooleanField(verbose_name='Status')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='Kategoria')),
                ('img', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_img', to='filer.Image')),
            ],
        ),
    ]
