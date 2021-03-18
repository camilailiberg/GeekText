from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def index(response, book_id):
    book = Book.objects.get(id=book_id)
    author = book.authors.all()
    ratings = book.ratings.all()
    average_rating = 0
    percent_rating = 0

    if len(ratings) != 0:

        for rate in ratings:
            average_rating += int(rate.rating)

        average_rating /= len(ratings)

        average_rating = round(average_rating, 1)

        percent_rating = (average_rating / 5) * 100


    return render(response, "bookdetails/book_detail.html", {'book': book,'author': author, 'ratings': ratings,
                                                             'average_rating': average_rating,
                                                             'percent_rating': percent_rating})


def home(response):
    return HttpResponse("<h1>hi</h1>")
    



