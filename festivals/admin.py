from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Country, Category, Tag, Artist, Festival


class FestivalAdminForm(forms.ModelForm):

    description = forms.CharField(widget=CKEditorWidget())


class CountryAdmin(admin.ModelAdmin):

    list_display = ('name', 'status',)  # lista pol w gridzie
    list_search = ['name', ]
    search_fields = ('name', 'status',)  # globalna wyszukiwarka


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'status',)
    list_search = ['name', ]
    search_fields = ('name', 'status',)


class TagAdmin(admin.ModelAdmin):

    list_display = ('name', 'url', 'status',)
    list_search = ['name', 'url']
    search_fields = ('name', 'url', 'status',)


class ArtistAdmin(admin.ModelAdmin):

    list_display = ('title', 'status',)
    list_search = ['title', ]
    search_fields = ('title', 'status',)


class FestivalAdmin(admin.ModelAdmin):

    change_list_template = 'admin/change_list_filter_sidebar.html'

    # pola w formularzu
    fieldsets = (
        ('', {
            'fields': ('title', 'country', 'address', 'category', 'artists', 'pub_date_start', 'pub_date_end', 'url', 'excerpt', 'description', 'user', 'tags',),
        }),
        ('Media', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('img',),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('seo_title', 'seo_keywords', 'seo_description',),
        }),

    )

    list_editable = ('pub_date_start', 'pub_date_end', 'url',)

    # lista pol w gridzie
    list_display = ('title', 'url', 'category',
                    'pub_date_start', 'pub_date_end',)

    # filtrowanie
    list_filter = ('category__name',)

    list_search = ['title', ]

    # globalna wyszukiwarka
    search_fields = ('title', 'url', 'category__name',)

    prepopulated_fields = {'url': ('title',)}

    raw_id_fields = ('category', 'country', 'tags', 'artists',)

    autocomplete_lookup_fields = {
        'fk': ['category', 'country', ],
        'm2m': ['tags', 'artists', ],
    }

    class StackedItemInline(admin.StackedInline):
        classes = ('grp-collapse grp-open',)

    class TabularItemInline(admin.TabularInline):
        classes = ('grp-collapse grp-open',)

    form = FestivalAdminForm

    # nadpisujemy pole uzytkkownika jesli nie zostalo wybrane
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.user:
            instance.user = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Festival, FestivalAdmin)
