from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import RatingReview
from .forms import RatingForm
from django.views.generic import TemplateView

# Create your views here.


def index(request, book_id):
    # Rating and Review Portion
    rating = RatingReview.objects.all()
    username = RatingReview.objects.all()
    form = RatingForm(request.POST or None)
    if form.is_valid():
        form.save()

    # Book Details Portion
    book = Book.objects.get(id=book_id)
    author = book.authors.all()
    ratings = book.ratings.all()
    average_rating = 0

    if len(ratings) != 0:

        for rate in ratings:
            average_rating += int(rate.rating)

        average_rating /= len(ratings)
        average_rating = round(average_rating, 1)

    context = {
        'form': form,
        'rating': rating,
        'username': username,
        'book': book, 'author': author,
        'ratings': ratings,
        'average_rating': average_rating
    }
    return render(request, "bookdetails/book_detail.html", context)


def home(response):
    return HttpResponse("<h1>hi</h1>")


    



