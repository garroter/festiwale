from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Slider, Slide


class SlideInline(admin.TabularInline):
    model = Slide


class SliderAdmin(admin.ModelAdmin):

    inlines = [
        SlideInline,
    ]
    
    list_display = ('title', 'status',)  # lista pol w gridzie
    list_search = ['title', ]
    search_fields = ('title', 'status',)  # globalna wyszukiwarka


class SlideAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'img', 'url', 'status',)
    list_search = ['title', 'description', 'img', 'url']
    search_fields = ('title', 'description', 'url', 'status',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Slide, SlideAdmin)
