from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from cart.models import Book


# Create your models here.

class WishList(models.Model):
    name = models.CharField(max_length=200)
    primary = models.BooleanField(True, False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist", null=True)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# class Book(models.Model):
#     wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
#     name = models.CharField(max_length=300)
#     added = models.BooleanField()
#
#     def __str__(self):
#         return self
