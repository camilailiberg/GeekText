from django.db import models
from django.core.exceptions import ValidationError


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

    def validate_rating(value):

        if value <= 5 and value >= 0:
            return value
        else:
            raise ValidationError("The rating is out of the bounds of 0 - 5")

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
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, validators=[validate_rating])
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.CharField(max_length=4000)
    publisher = models.CharField(max_length=200, default='Unknown')
    release_date = models.DateField(default='Unknown')

    def __str__(self):
        return self.title






