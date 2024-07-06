from django.db import models

class ArticlesModel(models.Model):
    image  = models.ImageField(upload_to='images/')
    text = models.TextField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article Done'
        verbose_name_plural = 'Articles Done'

    
class VisionsModel(models.Model):
    visions = models.CharField(max_length=1000)
    goals = models.CharField(max_length=1000)
    values = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Vision'
        verbose_name_plural = 'Visions'


class GroupArticlesModel(models.Model):
    image  = models.ImageField(upload_to='images/')
    text = models.TextField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Group'
        verbose_name = 'Groups'