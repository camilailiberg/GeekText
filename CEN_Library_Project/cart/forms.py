from django import forms

from .models import ShoppingCartItem


class CartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, required=False)

    class Meta:
        model = ShoppingCartItem
        fields = ('quantity',)
