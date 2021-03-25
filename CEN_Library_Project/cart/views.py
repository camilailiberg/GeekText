from django.shortcuts import render, redirect
from .models import ShoppingCart, ShoppingCartItem


# Create your views here.
def shoppingcartview(response):
    userid = response.user.id
    cart = ShoppingCart.objects.get(id=userid)
    if cart == response.user.shoppingcart:
        total = cart.subtotal()

        return render(response, "cart/shoppingcart.html", {"cart": cart, "total": total})

    message = "You tried to access an unautharized shopping cart"
    return render(response, "onlinelibrary/home.html", {"message": message})


def delete_cart_item(request, cartitemid):
    userid = request.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)

    if request.method == "POST":
        cartitem.delete()
        cart.save()
        return redirect('/ShoppingCart/')

    return render(request, "cart/deletecartitem.html", {"cartitem":cartitem})


def save_for_later(request, cartitemid):
    userid = request.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)

    if request.method == "POST":
        cartitem.savedforlater = True
        cartitem.save()

    cart.save()

    return redirect('/ShoppingCart/')


def move_to_cart(request, cartitemid):
    userid = request.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)

    if request.method == "POST":
        cartitem.savedforlater = False
        cartitem.save()

    cart.save()

    return redirect('/ShoppingCart/')


def update_quantity(request, cartitemid):
    userid = request.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)

    if request.method == "POST":
        newquantity = request.POST['UpdateValue']
        if int(newquantity) <= 0:
            raise Exception("new quantity must be greater than 0")
        cartitem.quantity = newquantity
        cartitem.save()
        cart.save()

    return redirect('/ShoppingCart/')


def checkout(request):
    userid = request.user.id
    cart = ShoppingCart.objects.get(id=userid)

    if request.method == "POST":
        for item in cart.shoppingcartitem_set.all():
            if not item.savedforlater:
                item.ordered = True
                item.save()
                cart.save()

    return redirect('/ShoppingCart/')


