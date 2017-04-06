# -*- encoding: utf-8 -*-
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from filer.fields.image import FilerImageField


class Country(models.Model):

    name = models.CharField(max_length=255, verbose_name="Kraj")
    status = models.BooleanField("Status")

    class Meta:
        verbose_name = 'Kraj'
        verbose_name_plural = 'Kraje'

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name="Kategoria")
    status = models.BooleanField("Status")

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=255, verbose_name="Tag")
    status = models.BooleanField("Status")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagi"

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Artist(models.Model):

    title = models.CharField(max_length=255, verbose_name="Tytuł", blank=True)
    url = models.SlugField('url', blank=True)
    excerpt = models.TextField(verbose_name="Krótki opis")
    description = RichTextUploadingField(blank=True)
    img = FilerImageField(null=True, blank=True, related_name="artist_img")
    seo_title = models.CharField(max_length=255, verbose_name="Seo tytuł :)", blank=True)
    seo_keywords = models.CharField(max_length=255, verbose_name="Seo słowa kluczowe :)", blank=True)
    seo_description = models.TextField(verbose_name="Seo opis :)", blank=True)
    status = models.BooleanField("Status")


    def get_absolute_url(self):
        return reverse('artist_details', kwargs={'url':self.url})


    class Meta:
        verbose_name = 'Artysta'
        verbose_name_plural = 'Artyści'
       

    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title


class Festival(models.Model):

    user = models.ForeignKey(User, verbose_name="Użytkownik", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria", blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Kraj", blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name="Tagi")
    artists = models.ManyToManyField(Artist, verbose_name="Artyści")
    url = models.SlugField('url', unique_for_date='pub_date_start', blank=True)
    title = models.CharField(verbose_name="Nazwa festiwalu", max_length=255)
    address = models.CharField(verbose_name="Adres", max_length=255)
    img = FilerImageField(null=True, blank=True, related_name="festiwal_img")
    excerpt = models.TextField(verbose_name="Krótki opis")
    description = RichTextUploadingField(blank=True, verbose_name="Opis")
    pub_date_start = models.DateTimeField("Data rozpoczęcia", blank=True, null=True)
    pub_date_end = models.DateTimeField("Data zakończenia", blank=True, null=True)
    seo_title = models.CharField(max_length=255, verbose_name="Seo tytuł :)", blank=True)
    seo_keywords = models.CharField(max_length=255, verbose_name="Seo słowa kluczowe :)", blank=True)
    seo_description = models.TextField(verbose_name="Seo opis :)", blank=True)

    def get_absolute_url(self):
        return reverse('festival_details', kwargs={'url':self.url})

    class Meta:
        verbose_name = "Festiwal"
        verbose_name_plural = "Festiwale"
        ordering = ("pub_date_start",)
        get_latest_by = "pub_date_start"

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

    def __str__(self):
        return self.title
