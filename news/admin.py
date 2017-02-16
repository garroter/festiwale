from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import News, Category, Tag

class NewsAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())


class NewsAdmin(admin.ModelAdmin):

    #lista pol w gridzie
    list_display = ('title', 'url')
    #pola w formularzu
    fieldsets = (
        ('', {
            'fields': ('url', 'user', 'category', 'tags', 'title', 'body', 'pub_date', 'status'),
        }),
        ('Media', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('img',),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('seo_title', 'seo_keywords', 'seo_description'),
        }),
      
    )

    #filtrowanie
    list_filter = ('category__name',)

    prepopulated_fields = {'url': ('title',)}

    raw_id_fields = ('category', 'tags')

    autocomplete_lookup_fields = {
        'fk': ['category',],
        'm2m': ['tags',],
    }

    class StackedItemInline(admin.StackedInline):
        classes = ('grp-collapse grp-open',)

    class TabularItemInline(admin.TabularInline):
        classes = ('grp-collapse grp-open',)

    form = NewsAdminForm

    # nadpisujemy pole uzytkkownika jesli nie zostalo wybrane
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.user:
            instance.user = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)

