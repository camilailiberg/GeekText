from django.db import models


class Book(models.Model):
    cover = models.ImageField(upload_to='bookImages', default='/Users/Christian/Desktop/No_image.jpg')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    GENRE = (
        ('Sci-Fi', 'Sci-Fi'),
        ('Fantasy', 'Fantasy'),
        ('Children', 'Children'),
        ('Other', 'Other'),
    )
    genre = models.CharField(max_length=200, choices=GENRE, default='Other')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.CharField(max_length=4000, blank=True)

    def __str__(self):
        return self.title

    def getprice(self):
        return self.price

    def __repr__(self):
        return '<Product object ({}) "{}" ${}>'.format(self.id, self.title, self.price)


class Author(models.Model):
    book = models.ManyToManyField(
        Book,
        related_name='authors',
    )
    author = models.CharField(max_length=200)
    bio = models.CharField(max_length=4000, blank=True)





