from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import WishList
from cart.models import ShoppingCart
from cart.models import ShoppingCartItem
from register.models import Profile
from bookdetails.models import Book

# Create your views here.

wishlist_id = 0


def index(response, id):  # good to go
    wl = WishList.objects.get(id=id)
    global wishlist_id
    wishlist_id = id
    bk = wl.book.all()
    return render(response, "wishlist/list.html", {"bk": bk})


def wishlist(response):  # good to go
    wl = WishList.objects.filter(user=response.user)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("new"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                if response.user.profile.wishlistCounter < 3:
                    response.user.profile.addWishlist()
                    response.user.profile.save()
                    wl.create(name=txt, primary=False, user=response.user)
                    return redirect('/wishlist/')
                else:
                    raise Exception("Maximum number of List")
            else:
                raise Exception("Invalid Name")

    return render(response, "wishlist/wishlisthome.html", {"wl": wl})


def delete_wishlist(request, id):  # good to go
    wl = WishList.objects.get(id=id)
    if request.method == "POST":
        wl.delete()
        request.user.profile.wishlistCounter = request.user.profile.wishlistCounter - 1
        request.user.profile.save()
        return redirect('/wishlist/')

    return render(request, "wishlist/delete.html", {'wl': wl})


def remove_book(request, id):  # good to go
    wl = WishList.objects.get(id=wishlist_id)
    bk = wl.book.get(id=id)
    if request.method == "POST":
        wl.book.remove(bk)
        return redirect('/wishlist/')

    return render(request, 'wishlist/remove.html', {"bk": bk})


def move_book(request, id):
    wl = WishList.objects.get(id=wishlist_id)
    bk = wl.book.get(id=id)
    if request.method == "POST":
        wl.book.id = wishlist_id
        return redirect('/wishlist/')

    return render(request, 'wishlist/transfer.html', {"bk": bk})


def move_to_cart(response, bookid):
    userid = response.user.id
    wl = WishList.objects.get(id=wishlist_id)
    bk = Book.objects.get(id=bookid)
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.all()
    cartitem.create(shoppingcart=cart, book=bk, quantity=1, ordered=False, savedforlater=False)
    wl.book.remove(bk)

    return redirect('/wishlist/')
