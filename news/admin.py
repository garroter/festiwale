from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import News, Category, Tag

class NewsAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())


class CategoryAdmin(admin.ModelAdmin):
    
    #lista pol w gridzie
    list_display = ('name', 'status',)

    list_search = ['name',]

    #globalna wyszukiwarka
    search_fields = ('name', 'status',)


class TagAdmin(admin.ModelAdmin):
    
    #lista pol w gridzie
    list_display = ('name', 'status',)

    list_search = ['name',]

    #globalna wyszukiwarka
    search_fields = ('name', 'status',)


class NewsAdmin(admin.ModelAdmin):
    
    change_list_template = "admin/change_list_filter_sidebar.html"

    #pola w formularzu
    fieldsets = (
        ('', {
            'fields': ('url', 'user', 'category', 'tags', 'festivals', 'title', 'body', 'pub_date', 'status',),
        }),
        ('Media', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('img',),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('seo_title', 'seo_keywords', 'seo_description',),
        }),
      
    )

    list_editable = ('status', 'pub_date', 'url',)

    #lista pol w gridzie
    list_display = ('title', 'url', 'category', 'pub_date', 'status',)

    #filtrowanie
    list_filter = ('category__name', 'status',)

    list_search = ['title',]

    #globalna wyszukiwarka
    search_fields = ('title', 'url','category__name', 'status',)

    prepopulated_fields = {'url': ('title',)}

    raw_id_fields = ('category', 'tags', 'festivals',)

    autocomplete_lookup_fields = {
        'fk': ['category',],
        'm2m': ['tags', 'festivals',],
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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(News, NewsAdmin)

