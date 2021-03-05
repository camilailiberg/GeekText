from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import WishList
from bookdetails.models import Book


# Create your views here.

def index(response, id):
    wl = WishList.objects.get(id=id)
    bk = wl.book.all()
    return render(response, "wishlist/list.html", {"bk": bk})


def wishlist(response):
    wl = WishList.objects.filter(user=response.user)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("new"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                wl.create(name=txt, primary=False, user=response.user)
            else:
                print("invalid")

    return render(response, "wishlist/wishlisthome.html", {"wl": wl})


def delete_wishlist(request, id):
    userid = request.user.id
    wl = WishList.objects.get(id=id)
    if request.method == "POST":
        wl.delete()
        return redirect('/wishlist/')

    return render(request, "wishlist/delete.html", {'wl': wl})


def remove_book(request, id):
    userid = request.user.id
    bk = Book.objects.get(id=id)
    if request.method == "POST":
        bk.delete()
        return redirect('/wishlist/')

    return render(request, 'wishlist/remove.html', {"bk": bk})


def move_book(response, bookid):
    userid = response.user.id
    wishlist = WishList.objects.get(id=userid)
    book = Book.objects.get(id=bookid)
    book.save()

    wishlist.save()

    return redirect('/')

def move_to_cart(response, bookid):
    userid = response.user.id
    wl = WishList.objects.get(id=userid)
    bk = Book.objects.get(id=bookid)
    bk.save()

    wl.save()

    return redirect('/wishlist/')
