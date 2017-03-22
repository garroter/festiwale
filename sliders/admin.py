from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Slider, Slide


class SlideInline(admin.TabularInline):
    model = Slide


class SliderAdmin(admin.ModelAdmin):
    
    inlines = [
        SlideInline,
    ]
    
    #lista pol w gridzie
    list_display = ('title', 'status',)

    list_search = ['title',]

    #globalna wyszukiwarka
    search_fields = ('title', 'status',)


class SlideAdmin(admin.ModelAdmin):
    
    #lista pol w gridzie
    list_display = ('title','description', 'img', 'url', 'status',)

    list_search = ['title', 'description', 'img', 'url']

    #globalna wyszukiwarka
    search_fields = ('title', 'description', 'url', 'status',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Slide, SlideAdmin)


