from django import forms
from django.utils.translation import gettext_lazy as _ 

PRODUCT_QAUNTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QAUNTITY_CHOICES,
        coerce=int,
        label=_('Quantity')
    )
    update = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
