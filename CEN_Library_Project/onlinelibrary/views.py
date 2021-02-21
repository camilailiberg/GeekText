from django.shortcuts import render
from .models import ShoppingCart
from .forms import ShoppingCartUpdate
from django.http import HttpResponse, request


# Create your views here.
def home(response):
    user = response.user
    return render(response, "onlinelibrary/home.html", {"user": user})


def shoppingcartview(response):
    userid = response.user.id
    cart = ShoppingCart.objects.get(id=userid)

    if cart == response.user.shoppingcart:
        total = 0
        for item in cart.shoppingcartitem_set.all():
            if not item.savedforlater and not item.ordered:
                total = total + item.total()

        return render(response, "onlinelibrary/shoppingcart.html", {"cart": cart, "total": total})

    message = "You tried to access an unautharized shopping cart"
    return render(response, "onlinelibrary/home.html", {"message": message})
