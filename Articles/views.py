from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *



def articles(request):
    template = loader.get_template('articles.html')
    if request.method == 'POST':
        param = request.POST.get('param')
        return redirect('result', param=int(param))
    articles = ArticlesModel.objects.all()
    visions = VisionsModel.objects.all()
    groups = GroupArticlesModel.objects.all()
    context = {
        'articles': articles,
        'MEDIA_URL': settings.MEDIA_URL,
        'visions': visions,
        'groups': groups,
    }
    return HttpResponse(template.render(context, request))

    
def result(request, param):
    articles = get_object_or_404(ArticlesModel, id=param)
    
    data = articles.text
    title = articles.title
    image = articles.image
    template = loader.get_template('result.html')
    
    context = {
        'Article': articles,
        'text': data,
        'MEDIA_URL': settings.MEDIA_URL,
        'title': title,
        'image_url': image,
    }
    
    return HttpResponse(template.render(context, request))

def test(request):
    articles = ArticlesModel.objects.all()
    #id = list(articles.ID)
    context = {
        'articles': articles,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    template = loader.get_template('test.html')
    for article in articles:
        print(article.id, article.image, article.text)
    return HttpResponse(template.render(context, request))
