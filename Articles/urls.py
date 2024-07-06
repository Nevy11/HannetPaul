from django.urls import path
from .views import *

app_name = 'Articles'


urlpatterns = [
    #path('', )
    path('articles', articles, name='articles'),
    path('result<int:param>/', result, name='result'),
    path('', test, name='test')
]