# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 18:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('festiwals', '0003_auto_20170216_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Tytuł')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('seo_title', models.CharField(blank=True, max_length=255, verbose_name='Seo tytuł :)')),
                ('seo_keywords', models.CharField(blank=True, max_length=255, verbose_name='Seo słowa kluczowe :)')),
                ('seo_description', models.TextField(blank=True, verbose_name='Seo opis :)')),
                ('status', models.BooleanField(verbose_name='Status')),
                ('img', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist_img', to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Artyści',
                'verbose_name': 'Artysta',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kategoria')),
                ('status', models.BooleanField(verbose_name='Status')),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
                'verbose_name': 'Kategoria',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kraj')),
                ('status', models.BooleanField(verbose_name='Status')),
            ],
            options={
                'verbose_name_plural': 'Kraje',
                'verbose_name': 'Kraj',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tag')),
            ],
            options={
                'verbose_name_plural': 'Tagi',
                'verbose_name': 'Tag',
            },
        ),
        migrations.RenameField(
            model_name='festiwal',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='festiwal',
            name='create_date',
        ),
        migrations.AddField(
            model_name='festiwal',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='img',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='festiwal_img', to='filer.Image'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='pub_date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data zakończenia'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='pub_date_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data rozpoczęcia'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='seo_description',
            field=models.TextField(blank=True, verbose_name='Seo opis :)'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=255, verbose_name='Seo słowa kluczowe :)'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='seo_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Seo tytuł :)'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='url',
            field=models.SlugField(blank=True, unique_for_date='pub_date_start', verbose_name='url'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='artists',
            field=models.ManyToManyField(to='festiwals.Artist', verbose_name='Artyści'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='festiwals.Category', verbose_name='Kategoria'),
        ),
        migrations.AddField(
            model_name='festiwal',
            name='tags',
            field=models.ManyToManyField(to='festiwals.Tag', verbose_name='Tagi'),
        ),
    ]