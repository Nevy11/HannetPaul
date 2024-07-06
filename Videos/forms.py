from django import forms
from django.forms import ModelForm
from .models import *

class VideoUploadForm(ModelForm):
    class Meta:
        model = VideosModel
        fields = ['title', 'description', 'userImage', 'video']