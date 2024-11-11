from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
def bookhome(request):
    searchTerm=request.GET.get('searchBook')
    if searchTerm:
        book_list = Book.objects.filter(title__contains=searchTerm)
    else:
        book_list = Book.objects.all()
    paginator = Paginator(book_list, 1)
    page_number = request.GET.get('page', 1)
    movies = paginator.page(page_number)
    return render(request,'bookhome.html',
                  {'searchTerm':searchTerm,'books':book_list})
def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookdetail.html', {'book': book})
