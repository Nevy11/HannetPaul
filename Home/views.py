#from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf import settings


def choice(request):
    template = loader.get_template('home.html')
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))


def user(request):
    template = loader.get_template('user.html')
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))