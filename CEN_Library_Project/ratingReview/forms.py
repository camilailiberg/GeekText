from typing import Any

from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, Textarea
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BookRating

RATE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
     )
class RatingForm(forms.ModelForm):

    class Meta:
        model = BookRating
        fields = [
            'rating',
            'name',
            'username',
            'id',
        ]
        widgets = {'rating' : forms.RadioSelect, 'name' : Textarea}



