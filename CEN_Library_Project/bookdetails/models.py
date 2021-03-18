from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=200)
    bio = models.CharField(max_length=4000)

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






