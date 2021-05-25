from django.db.models import fields
from django import forms
from django.forms.widgets import DateInput, DateTimeInput
from .models import Product
from functools import partial


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["auctoneer"]
