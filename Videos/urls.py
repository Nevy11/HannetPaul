from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'Videos'

urlpatterns = [
    path('', videos, name='videos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)