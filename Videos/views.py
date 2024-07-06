from django.shortcuts import redirect, render
from django.conf import settings
from .forms import VideoUploadForm
from .models import VideosModel

def videos(request):
    #searchForm = SearchVideoModelForm()
    form = VideoUploadForm
    
    videos = VideosModel.objects.all()
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'videos': videos,
        'form': form,
    }
    
    return render(request, 'videos.html', context)

def searchVideo(request):
    return HttpResponse('<h1>Video Not Found</h1>')
