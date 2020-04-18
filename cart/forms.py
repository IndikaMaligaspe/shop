from django import forms

PRODUCT_QAUNTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QAUNTITY_CHOICES,
        coerce=int
    )
    update = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
