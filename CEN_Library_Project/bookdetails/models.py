from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Author(models.Model):
    author = models.CharField(max_length=200)
    bio = models.CharField(max_length=4000)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return self.author


class Book(models.Model):

    authors = models.ManyToManyField(
        Author,
        related_name='booker',
    )

    GENRES = (
        ('Sci-fi', 'Sci-fi'),
        ('Fantasy', 'Fantasy'),
        ('Children', 'Children'),
        ('Non-fiction', 'Non-fiction'),
        ('Others', 'Others'),
    )

    cover = models.ImageField(upload_to='bookImages', default='bookImages/No_image.jpg')
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, default='other', choices=GENRES)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.CharField(max_length=4000)
    publisher = models.CharField(max_length=200, default='Unknown')
    release_date = models.DateField(default='Unknown')
    bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Rating and Review Portion
class RatingReview(models.Model):
    RATE = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )
    book = models.ForeignKey("Book", on_delete=models.CASCADE, default=0, related_name="ratings")
    rating = models.CharField(choices=RATE, max_length=128, default=1)
    review = models.CharField(max_length=128, default='Write Review')
    username = models.CharField(max_length=128, default="")
    nickName = models.BooleanField(default=False)
    first_name = models.CharField(max_length=128, default="")
    last_name = models.CharField(max_length=128, default="")
    book_title = models.CharField(max_length=128, default="")
    anonymous = models.BooleanField(default=False)


    def str(self):
        return self.rating

    class Meta:
        managed = True
        db_table = 'ratingReview_bookdetails'





