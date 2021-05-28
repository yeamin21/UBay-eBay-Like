
from django.contrib import admin

from gallery.models import Product


class ProductModel(admin.ModelAdmin):
    list_display = ['name','created_at']

# Register your models here.

admin.site.register(Product,ProductModel)
