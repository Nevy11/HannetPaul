from django import forms
from django.forms import ModelForm
from .models import *


class BooksModelForm(ModelForm):
    class Meta:
        model = BooksModel
        fields = ['title', 'genre','image', 'book']
    