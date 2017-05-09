# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from festivals.models import Festival
from ckeditor_uploader.fields import RichTextUploadingField
from filer.fields.image import FilerImageField


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Kategoria')
    status = models.BooleanField('Status')

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'name__icontains',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=255, verbose_name='Tag')
    url = models.SlugField('url', blank=True)
    status = models.BooleanField('Status')

    def get_absolute_url(self):
        return reverse('news_tags', kwargs={'url': self.url})

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'name__icontains',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class News(models.Model):

    user = models.ForeignKey(User, verbose_name='Użytkownik', blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Kategoria', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tagi')
    festivals = models.ManyToManyField(Festival, verbose_name='Festiwale')
    url = models.SlugField('url', unique_for_date='pub_date', blank=True)
    title = models.CharField(max_length=255, verbose_name='Tytuł', blank=True)
    excerpt = models.TextField(verbose_name='Krótki opis')
    body = RichTextUploadingField(blank=True)
    pub_date = models.DateTimeField('Data publikacji', blank=True, null=True)
    img = FilerImageField(null=True, blank=True, related_name='news_img')
    seo_title = models.CharField(
        max_length=255, verbose_name='Seo tytuł :)', blank=True)
    seo_keywords = models.CharField(
        max_length=255, verbose_name='Seo słowa kluczowe :)', blank=True)
    seo_description = models.TextField(verbose_name='Seo opis :)', blank=True)
    status = models.BooleanField('Status')

    def get_absolute_url(self):
        return reverse('news_details', kwargs={'url': self.url})

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
