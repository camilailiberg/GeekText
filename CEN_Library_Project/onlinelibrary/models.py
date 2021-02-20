from django.db import models

# Create your models here.

class WishList(models.Model):
    name = models.CharField(max_length=200)
    primary = models.BooleanField(True, False)
    max = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Book(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    added = models.BooleanField()

    def __str__(self):
        return self.name
