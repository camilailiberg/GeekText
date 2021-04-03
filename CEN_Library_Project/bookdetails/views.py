from django.shortcuts import render
from .models import Book
from .models import Author
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
    percent_rating = 0

    if len(ratings) != 0:

        for rate in ratings:
            average_rating += int(rate.rating)

        average_rating /= len(ratings)
        average_rating = round(average_rating, 1)
        percent_rating = (average_rating / 5) * 100

    context = {
        'form': form,
        'rating': rating,
        'username': username,
        'book': book, 'author': author,
        'ratings': ratings,
        'average_rating': average_rating,
        'percent_rating': percent_rating
    }
    return render(request, "bookdetails/book_detail.html", context)


def similar(request, author):
    writer = Author.objects.get(author=author)
    books = Book.objects.filter(authors=writer)
    return render(request, "bookdetails/similar_author.html", {'book': books, 'author': author})

    



