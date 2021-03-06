from django.contrib import admin
from .models import BookRating
from bookdetails.models import Book, Author

# Register your models here.
admin.site.register(BookRating)
