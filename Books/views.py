import os
from django.template import loader
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.dispatch import receiver
from django.core.signals import request_finished
from docx import Document
from weasyprint import HTML
from .forms import *
from .models import *

generated_files = []

@receiver(request_finished)
def cleanup_files(sender, **kwargs):
    global generated_files
    for filePath in generated_files:
        if os.path.exists(filePath):
            os.remove(filePath)
    generated_files = []

def books(request):
    template = loader.get_template('books.html')
    books = BooksModel.objects.all()
    unique = BooksModel.objects.distinct('genre')
    if request.method == 'POST':
        return redirect('result', id=int(book_id))
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'books': books,
        'unique': unique,
    }
    return HttpResponse(template.render(context, request))

def booksUploading(request):
    if request.method == 'POST':
        form = BooksModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Books:bookList')
    else:
        form = BooksModelForm()
    template = loader.get_template('booksUploading.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def bookList(request):
    books = BooksModel.objects.all()
    template = loader.get_template('bookList.html')
    context = {}
    return HttpResponse(template.render(context, request))

def novel(request, book_id):
    books = get_object_or_404(BooksModel, id=book_id)
    template = loader.get_template('novel.html')
    
    context = {
        'books': books,
        'MEDIA_URL': settings.MEDIA_URL,    
    }
    return HttpResponse(template.render(context, request))

def convert_docx_to_pdf(filePath):
    document = Document(filePath)
    html_content = "<html><body>"
    for paragraph in document.paragraphs:
        html_content += f"<p>{paragraph.text}</p>"
    html_content += "</body></html>"
    
    pdf_file_path = filePath.replace('.docx', '.pdf')
    HTML(string=html_content).write_pdf(pdf_file_path)
    generated_files.append(pdf_file_path)
    return pdf_file_path

def viewBook(request, bookId):
    books = get_object_or_404(BooksModel, id=bookId)
    filename = books.book.name
    filePath = os.path.join(settings.MEDIA_ROOT, filename)
    if not os.path.exists(filePath):
        raise Http404('File does not exist')
    
    if filename.endswith('.docx'):
        filePath = convert_docx_to_pdf(filePath)
    
    return FileResponse(open(filePath, 'rb'), content_type='application/pdf', as_attachment=False, filename=os.path.basename(filePath))
