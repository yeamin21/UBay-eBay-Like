from django.db.models import fields
from django import forms
from django.forms.widgets import DateInput, DateTimeInput
from .models import Product


class CreateProductForm(forms.ModelForm):
    ends_at = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(
            attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}
        )
    )

    class Meta:
        model = Product
        exclude = ["auctoneer"]
