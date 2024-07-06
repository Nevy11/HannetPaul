from django.contrib import admin
from .models import *


class BooksModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre','image', 'book')


admin.site.register(BooksModel, BooksModelAdmin)
