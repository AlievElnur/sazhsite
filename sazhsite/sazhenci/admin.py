from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class RasteniyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'lef', 'content', 'photo', 'get_html_photo', 'is_published')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Мини-фотка'

class LeftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Rasteniya, RasteniyaAdmin)
admin.site.register(Left, LeftAdmin)

admin.site.site_title = 'Админка сайта о саженцах'
admin.site.site_header = 'Админка сайта о саженцах 2'
