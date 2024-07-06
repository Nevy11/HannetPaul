from django.db import models


class VideosModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    userImage = models.ImageField(upload_to='userImage/')
    video = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = "Videos"