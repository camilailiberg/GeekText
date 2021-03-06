from django import forms
from django.forms import ModelForm
from bookdetails.models import Book

class BookForm(ModelForm):

    allTuple = (('Select All', 'Select All'),)
    genre_choice_empty = allTuple + Book.GENRE
    genre = forms.ChoiceField(choices=genre_choice_empty, label='Filter by Genre')

    class Meta:
            model = Book
            fields = ['genre']