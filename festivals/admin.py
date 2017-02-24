from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Country, Category, Tag, Artist, Festival

class CountryAdmin(admin.ModelAdmin):
    
    #lista pol w gridzie
    list_display = ('name', 'status',)

    list_search = ['name',]

    #globalna wyszukiwarka
    search_fields = ('name', 'status',)

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


class ArtistAdmin(admin.ModelAdmin):

    #lista pol w gridzie
    list_display = ('title', 'status',)

    list_search = ['title',]

    #globalna wyszukiwarka
    search_fields = ('title', 'status',)


class FestivalAdmin(admin.ModelAdmin):

    change_list_template = "admin/change_list_filter_sidebar.html"

    #pola w formularzu
    fieldsets = (
        ('', {
            'fields': ('url', 'category', 'tags', 'artists', 'title', 'description', 'pub_date_start', 'pub_date_end',),
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

    list_editable = ('pub_date_start', 'pub_date_end', 'url',)

    #lista pol w gridzie
    list_display = ('title', 'url', 'category', 'pub_date_start', 'pub_date_end',)

    #filtrowanie
    list_filter = ('category__name',)

    list_search = ['title',]

    #globalna wyszukiwarka
    search_fields = ('title', 'url','category__name',)

    prepopulated_fields = {'url': ('title',)}

    raw_id_fields = ('category', 'tags', 'artists',)

    autocomplete_lookup_fields = {
        'fk': ['category',],
        'm2m': ['tags', 'artists', ],
    }

    class StackedItemInline(admin.StackedInline):
        classes = ('grp-collapse grp-open',)

    class TabularItemInline(admin.TabularInline):
        classes = ('grp-collapse grp-open',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Festival, FestivalAdmin)
