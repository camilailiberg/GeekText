from django.shortcuts import render
from bookdetails.models import Book
from . import forms
# Create your views here.
def post_list(request):

    books = Book.objects.all()
    book_form = forms.BookForm()
    book_form.fields['genre'].initial = dict(book_form.genre_choice_empty)['Select All']
    star_select = 0

    if request.method == "GET":
        genre_query = request.GET.get('genre')
        rating_query = request.GET.get('rate')
        title_query = request.GET.get('title')

        if genre_query is None or genre_query == 'Select All':
            books = Book.objects.all()
        else:
            books = books.filter(genre=genre_query)
            book_form.fields['genre'].initial = dict(book_form.genre_choice_empty)[genre_query]

        if title_query is not None:
            books = books.filter(title__icontains=title_query)

        if rating_query is not None:
            books = books.filter(rating__gte=rating_query)
            star_select = rating_query

        args = {'books': books, 'book_form': book_form, 'star_select': star_select, }

    return render(request, 'browse/post_list.html', args)
