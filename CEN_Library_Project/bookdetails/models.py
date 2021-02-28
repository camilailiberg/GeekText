import uuid
from django.contrib.auth import get_user_model
from django.db import models


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    cover = models.ImageField(upload_to='bookImages', default='/Users/Christian/Desktop/No_image.jpg')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, default='other')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=4000, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review


class Author(models.Model):
    book = models.ManyToManyField(
        Book,
        related_name='authors',
    )
    author = models.CharField(max_length=200)
    bio = models.CharField(max_length=4000, blank=True)





