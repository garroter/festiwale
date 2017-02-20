from django.db import models

class Festiwal(models.Model):
    name = models.CharField(verbose_name="Nazwa festiwalu", max_length=255)
    create_date = models.DateTimeField("Data utowrzenia")

    class Meta:
        verbose_name = "Festiwal"
        verbose_name_plural = "Festiwale"

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

    def __str__(self):
        return self.name
