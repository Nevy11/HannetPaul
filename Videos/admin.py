from django.contrib import admin
from .models import *


class VideosModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'userImage', 'video')


admin.site.register(VideosModel, VideosModelAdmin)