from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from cart.models import ShoppingCart
from bookdetails.models import Book


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
    address = models.CharField(max_length=200)
    homeAddress = models.CharField(max_length=200)
    # Changes I made


    wishlistCounter = models.IntegerField(default=0)
    # booksbought = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="booksbought", null=True) # TODO: I changed this, talk to Pedro

    def __str__(self):
        return self.user.username

    def addWishlist(self):
        self.wishlistCounter = self.wishlistCounter + 1

    def createprofile(sender, instance, created, **kwargs):

        if created:
            userid = instance.id
            Profile.objects.create(user=instance, id=userid)
            ShoppingCart.objects.create(user=instance, id=userid)

            print('Profile and Shopping Cart Created!')

    post_save.connect(createprofile, sender=User)


class CreditCard(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cardnumber = models.IntegerField(default=0)
    expiration = models.DateField()
    security = models.IntegerField(default=0)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):

        return self.cardnumber

        return str(self.cardnumber)


