from django.contrib import admin
from .models import Book, ShoppingCart, ShoppingCartItem

# Register your models here.
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
admin.site.register(Book)

