from typing import Any

from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, Textarea
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RatingReview

RATE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class RatingForm(forms.ModelForm):
    class Meta:
        model = RatingReview
        fields = [
            'rating',
            'username',
            'review',
            'book',
            'nickName',
            'anonymous',
            'first_name',
            'last_name',
            'book_title'
        ]
        widgets = {'rating': forms.RadioSelect, 'review': Textarea, 'book': Textarea}
