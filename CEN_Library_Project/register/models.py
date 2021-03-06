from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from cart.models import ShoppingCart


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
    address = models.CharField(max_length=200)
    homeAddress = models.CharField(max_length=200)
    #creditCard = models.IntegerField() # TODO: MAx and min length
    wishlistCounter = models.IntegerField(default=0)


    def str(self):
        return self.user.username

    def addWishlist(self):

        self.wishlistCounter + 1


    def createprofile(sender, instance, created, **kwargs):

        if created:
            userid = instance.id
            Profile.objects.create(user=instance, id=userid)
            ShoppingCart.objects.create(user=instance, id=userid)
            print('Profile Created!')

    post_save.connect(createprofile, sender=User)