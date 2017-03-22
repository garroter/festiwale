from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from filer.fields.image import FilerImageField



class Slider(models.Model):

    title = models.CharField(max_length=255, verbose_name="Tytuł")
    home = models.BooleanField("Strona główna")
    status = models.BooleanField("Status")

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slidery"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Slide(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, verbose_name="Slider", null=True)
    title = models.CharField(max_length=255, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    img = FilerImageField(null=True, blank=True, related_name="slide_img")
    url = models.SlugField('url', blank=True)
    status = models.BooleanField("Status")
