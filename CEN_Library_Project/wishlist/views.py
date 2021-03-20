from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import WishList
from bookdetails.models import Book
from cart.models import ShoppingCart
from cart.models import ShoppingCartItem


# Create your views here.


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
                wl.create(name=txt, primary=False, user=response.user)
                return redirect('/wishlist/')
            else:
                raise Exception("Invalid Name")

    return render(response, "wishlist/wishlisthome.html", {"wl": wl})


def delete_wishlist(request, id):  # good to go
    wl = WishList.objects.get(id=id)
    if request.method == "POST":
        wl.delete()
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

    # for every shoppingcartitem in the cart object of the user
    for item in cart.shoppingcartitem_set.all():
        #  if the item is not marked as ordered and the book saved in the shoppingcartitem object
        # is the same book that we are moving from wishlist
        if item.ordered == False and item.book == bk:
            item.quantity = item.quantity + 1  # Update the quantity of that shippingcartitem
            if item.savedforlater: #  if the shoppingcartitem object that holds the book being moved is in the
                # saved for later section of the shopping cart
                item.savedforlater = False #  take it out of the saved for later section and move it to the main
                # section of the shopping cart
            item.save()
            cart.save()
            wl.book.remove(bk)
            return redirect('/wishlist/')
    cartitem = ShoppingCartItem.objects.all()
    cartitem.create(shoppingcart=cart, book=bk, quantity=1, ordered=False, savedforlater=False)
    wl.book.remove(bk)
    return redirect('/wishlist/')
