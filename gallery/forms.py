import datetime
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime, AdminTimeWidget
from django.db.models import fields
from django import forms
from .models import Product
from django.contrib.admin import widgets


class CreateProductForm(forms.ModelForm):
    ends_at = forms.DateTimeField(initial=datetime.datetime.now)

    class Meta:
        model = Product
        exclude = ["auctoneer"]
