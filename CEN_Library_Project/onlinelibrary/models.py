from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def getprice(self):
        return self.price

    def __repr__(self):
        return '<Product object ({}) "{}" ${}>'.format(self.id, self.name, self.price)


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shoppingcart", null=True)

    def __str__(self):
        return str(self.user.username) + "'s cart"

    def subtotal(self):
        amount = 0.0
        for cartitem in self.shoppingcartitem_set:
            amount = amount + (cartitem.quantity * cartitem.book.getprice())
        return round(amount, 2)

    def createshoppingcart(sender, instance, created, **kwargs):

        if created:
            userid = instance.id
            ShoppingCart.objects.create(user=instance, id=userid)
            print('ShoppingCart Created!')

    post_save.connect(createshoppingcart, sender=User)

    def __repr__(self):
        return '<ShoppingCart object ({}) "{}">'.format(self.id, self.user.username)


class ShoppingCartItem(models.Model):
    shoppingcart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered = models.BooleanField(default=False)
    addedon = models.DateField(auto_now_add=True)
    purchasedby = models.DateField(auto_now=True)
    savedforlater = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name

    def total(self):
        return round(self.quantity * self.book.getprice(), 2)

    def getbookname(self):
        return self.book.name

    def getusername(self):
        return self.shoppingcart.user.username

    def getuserid(self):
        return self.shoppingcart.user.id

    def __repr__(self):
        return '<ShoppingCartItem object ({}) {}x "{}" "{}" {} {} {} {}>'.format(self.id, self.quantity, self.book.name,
                                                                                 self.shoppingcart.user.username,
                                                                                 self.ordered,
                                                                                 self.addedon, self.savedforlater,
                                                                                 self.purchasedby)