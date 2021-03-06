from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def index(response, book_id):
    book = Book.objects.get(id=book_id)
    author = book.authors.all()
    return render(response, "bookdetails/book_detail.html", {'book': book, 'author': author})


def home(response):
    return HttpResponse("<h1>hi</h1>")
    



