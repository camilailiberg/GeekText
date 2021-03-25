from django.db.models.query import QuerySet
from django.shortcuts import render
from bookdetails.models import Book, Author
from django.core.paginator import Paginator

from . import forms
# Create your views here.
def post_list(request):

    book_form = forms.BookForm()
    book_form.fields['genre'].initial = dict(book_form.genre_choice_empty)['Select All']
    star_select = 0
    attach_url = ""

    if request.method == "GET":
        genre_query = request.GET.get('genre')
        rating_query = request.GET.get('rate')
        title_query = request.GET.get('title')
        page_number = request.GET.get('page')
        submit_query = request.GET.get('submit')
        sortby_query = request.GET.get('sortBy')
        sortorder_query = request.GET.get('sortOrder')
        print(request.GET.get('booksPerPage'))

        if request.GET.get('booksPerPage') is None:
            booksPerPage= 10
            page_select = 0
        elif request.GET.get('booksPerPage') == '10':
            booksPerPage = 10
            page_select = 10
            attach_url += "&booksPerPage=" + str(booksPerPage)
        else:
            booksPerPage = 20
            page_select = 20
            attach_url += "&booksPerPage=" + str(booksPerPage)

        if (genre_query is None and submit_query is None) or (genre_query == 'Select All'):
            books = Book.objects.all().order_by('id')
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
        else:
            books = Book.objects.order_by('id')
            books = books.filter(genre=genre_query)
            book_form.fields['genre'].initial = dict(book_form.genre_choice_empty)[genre_query]
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
            attach_url += "&genre=" + genre_query

        if title_query is not None:
            books = books.filter(title__icontains=title_query)
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
            attach_url += "&title=" + title_query

        if rating_query is not None:
            books = books.filter(rating__gte=rating_query)
            star_select = rating_query
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
            attach_url += "&rate=" + rating_query

        if sortby_query is not None:
            if sortorder_query is None or sortorder_query == 'ascend':
                books = books.filter().order_by(sortby_query)
            else:
                sortby_query = '-' + sortby_query
                books = books.filter().order_by(sortby_query)
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
            attach_url += "&sortBy=" + sortby_query

        args = {'books_page': books_page, 'book_form': book_form, 'star_select': star_select, 'title_query': title_query}
        args2 = {'genre_query': genre_query, 'attach_url': attach_url, 'page_select': page_select}
    return render(request, 'browse/post_list.html', {**args, **args2})
