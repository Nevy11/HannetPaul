from django.contrib import admin
from .models import *


class ArticlesModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'text', 'title', 'description')
    #fields = ('image', 'text')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 150px;"/>'.format(obj.image.url))

admin.site.register(ArticlesModel, ArticlesModelAdmin)


class VisionsModelAdmin(admin.ModelAdmin):
    list_display = ('visions', 'goals', 'values')


admin.site.register(VisionsModel, VisionsModelAdmin)


class GroupArticlesModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'text', 'title', 'description')


admin.site.register(GroupArticlesModel, GroupArticlesModelAdmin)