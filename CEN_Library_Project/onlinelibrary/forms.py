from django import forms

from .models import ShoppingCartItem


class CartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, required=False)
    savedforlater = forms.BooleanField(label="Save for later", required=False)

    class Meta:
        model = ShoppingCartItem
        fields = ('quantity', 'savedforlater')
