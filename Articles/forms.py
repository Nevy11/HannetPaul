from django.forms import ModelForm
from django import forms
from .models import *

class ArticlesModelForm(ModelForm):
    class Meta:
        model = ArticlesModel
        fields = ['image', 'text']