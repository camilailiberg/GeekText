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
        sortby_query = request.GET.get('sortBy')
        sortorder_query = request.GET.get('sortOrder')
        bestSeller = request.GET.get('bestSeller')

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

        books = Book.objects.all().order_by('id')
        if bestSeller == 'best':
            books = books.filter(bestseller=True)#Book.objects.filter(bestseller=True)
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
        if (genre_query is None) or (genre_query == 'Select All'):
            books = books.filter().order_by('id')#Book.objects.all().order_by('id')
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
        else:
            #books = Book.objects.order_by('id')
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
            books_rating_filter = []
            for book in books:
                if book.average_rating >= float(rating_query):
                    books_rating_filter.append(book.id)
            books = books.filter(id__in=books_rating_filter)
            star_select = rating_query
            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
            attach_url += "&rate=" + rating_query

        if sortby_query is not None:
            if sortorder_query is None or sortorder_query == 'ascend':
                if sortby_query != 'authors':
                    if sortby_query != 'rating':
                        books = books.filter().order_by(sortby_query)
                    else:
                        books_rating_sort = []
                        for book in books:
                            books_rating_sort.append(book)
                        books_rating_sort.sort(key=lambda rating: rating.average_rating)
                        books = books_rating_sort
                else:
                    books = books.filter().order_by(sortby_query)
                    books_no_duplicate = []
                    for book in books:
                        books_no_duplicate.append(book)
                    books_no_duplicate = list(dict.fromkeys(books_no_duplicate))
                    print(books_no_duplicate)
                    books = books_no_duplicate
                attach_url += "&sortOrder=" + str(sortorder_query)
            else:
                if sortby_query != 'authors':
                    if sortby_query != 'rating':
                        books = books.filter().order_by('-' + sortby_query)
                    else:
                        books_rating_sort = []
                        for book in books:
                            books_rating_sort.append(book)
                        books_rating_sort.sort(key=lambda rating: rating.average_rating, reverse=True)
                        books = books_rating_sort
                else:
                    books = books.filter().order_by('-' + sortby_query)
                    books_no_duplicate = []
                    for book in books:
                        books_no_duplicate.append(book)
                    books_no_duplicate = list(dict.fromkeys(books_no_duplicate))
                    books = books_no_duplicate
                    print(books)
                attach_url += "&sortOrder=" + sortorder_query

            paginator = Paginator(books, booksPerPage)
            books_page = paginator.get_page(page_number)
            attach_url += "&sortBy=" + sortby_query
            attach_url += "&bestSeller=" + str(bestSeller)

        args = {'books_page': books_page, 'book_form': book_form, 'star_select': star_select, 'title_query': title_query}
        args2 = {'genre_query': genre_query, 'attach_url': attach_url, 'page_select': page_select}
        args3 = {'bestSeller': bestSeller, 'sortOrder': sortorder_query}
    return render(request, 'browse/post_list.html', {**args, **args2, **args3})
