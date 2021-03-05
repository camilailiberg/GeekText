from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from bookdetails.models import Book


# Create your models here.

class WishList(models.Model):
    name = models.CharField(max_length=200)
    primary = models.BooleanField(True, False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist", null=True)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

    def getuserid(self):
        return self.user.id

    def getbookid(self):
        return self.book


#class WishListItems(models.Model):
