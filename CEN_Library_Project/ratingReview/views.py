from django.shortcuts import render
from django.http import HttpResponse
from .models import BookRating
from .forms import RatingForm
from django.contrib.auth.decorators import login_required
from .models import BookRating
from cart.models import ShoppingCart

# Create your views here.

def rating_create_view(request):
    rating = BookRating.objects.all()
    username = BookRating.objects.all()
    form = RatingForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        'rating': rating,
        'username': username
    }
    return render(request, "home.html", context)
