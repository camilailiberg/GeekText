from django.contrib import admin
from .models import Book, Author, RatingReview

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(RatingReview)
