from django.shortcuts import render
from django.http import HttpResponse
from .models import BookRating
from .forms import RatingForm
from django.contrib.auth.decorators import login_required
from .models import BookRating
from cart.models import ShoppingCart


# Create your views here.
# def rating_create_view(request):
#     rating = BookRating.objects.all()
#     username = BookRating.objects.all()
#     form = RatingForm(request.POST)
#     cartitems = request.user.ShoppingCart_shoppingcartitem.all()
#     context = {
#         'form': form,
#         'rating': rating,
#         'username': username
#     }
#     counter = 0
#     if form.is_valid():
#         for book in cartitems:
#             counter = counter + 1
#         if counter > 0:
#             form.save()
#         else:
#             return render(request, "home.html", context)
#
#     return render(request, "home.html", context)


def rating_create_view(request):
    rating = BookRating.objects.all()
    username = BookRating.objects.all()
    form = RatingForm(request.POST)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        'rating': rating,
        'username': username
    }
    return render(request, "home.html", context)
