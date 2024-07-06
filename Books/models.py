from django.db import models


class BooksModel(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    book = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
