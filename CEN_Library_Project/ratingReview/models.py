from django.db import models
from django.conf import settings
from django import forms
from django.contrib.auth.models import User
from cart.models import ShoppingCart


class BookRating(models.Model):

    # book = models.ForeignKey("bookdetails.Book", on_delete=models.CASCADE, default=0, related_name="ratings")


    RATE = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )

    rating = models.CharField(choices=RATE, max_length=128, default = 1)
    review = models.CharField(max_length=128, default='Write Review')
    username = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.rating

    class Meta:
        managed = True
        db_table = 'ratingReview_bookrating'











