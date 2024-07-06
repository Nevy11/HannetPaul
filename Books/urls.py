from django.urls import path
from .views import *

app_name = 'Books'

urlpatterns = [
    path('', books, name='books'),
    path('booksUploading/', booksUploading, name='booksUploading'),
    path('bookList/', bookList, name='bookList'),
    path('novel<int:book_id>/', novel, name='novel'),
    path('viewBook<int:bookId>/', viewBook, name='viewBook'),
]