from django import forms


class ShoppingCartUpdate(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    savedforlater = forms.BooleanField(label="Save for later", required=False)
    remove = forms.BooleanField(label="Remove", required=False)
