from django.shortcuts import render, redirect
from django import forms
from .models import Book
from .models import Author
from .models import RatingReview
from .forms import RatingForm
from .forms import RatingFormAnon
from cart.models import ShoppingCart, ShoppingCartItem
# from cart.views import *
from ratingReview.forms import RatingForm
from cart.views import *

from django.views.generic import TemplateView


# Create your views here.
def index(request, book_id):
    # Rating and Review Portion
    rating = RatingReview.objects.all()
    username = RatingReview.objects.all()
    bookPurchase = ShoppingCartItem.objects.all()
    form1 = RatingForm(request.POST or None)
    form2 = RatingFormAnon(request.POST or None)

    if form1.is_valid():
        form1.save()

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
        'form1': form1,
        'form2': form2,
        'rating': rating,
        'username': username,
        'book': book, 'author': author,
        'ratings': ratings,
        'average_rating': average_rating,
        'percent_rating': percent_rating,
        'bookPurchase': bookPurchase
    }

    return render(request, "bookdetails/book_detail.html", context)


def similar(request, author):
    writer = Author.objects.get(author=author)
    books = Book.objects.filter(authors=writer)
    return render(request, "bookdetails/similar_author.html", {'book': books, 'author': author})


def move_book_to_cart(request, bookid):
    userid = request.user.id
    bk = Book.objects.get(id=bookid)
    cart = ShoppingCart.objects.get(id=userid)

    if request.method == "POST":
        # for every shoppingcartitem in the cart object of the user
        for item in cart.shoppingcartitem_set.all():
            #  if the item is not marked as ordered and the book saved in the shoppingcartitem object
            # is the same book that we are moving from wishlist
            if item.ordered == False and item.book == bk:
                item.quantity = item.quantity + 1  # Update the quantity of that shippingcartitem
                if item.savedforlater:  # if the shoppingcartitem object that holds the book being moved is in the
                    # saved for later section of the shopping cart
                    item.savedforlater = False  # take it out of the saved for later section and move it to the main
                    # section of the shopping cart
                item.save()
                cart.save()
                return redirect('index', bookid)
        cartitem = ShoppingCartItem.objects.all()
        cartitem.create(shoppingcart=cart, book=bk, quantity=1, ordered=False, savedforlater=False)
        return redirect('index', bookid)


