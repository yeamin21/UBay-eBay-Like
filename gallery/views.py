
from user.models import User
from django.http import request
from django.views.generic.detail import SingleObjectMixin
from gallery.forms import CreateProductForm
from gallery.models import Product
from django.db.models.base import Model
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductList(LoginRequiredMixin, ListView):
    login_url = '/auth/login'
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.all()

    def get_queryset(self):
        try:
            auctoneer = User.objects.get(email=self.kwargs['user'])
            return self.queryset.filter(auctoneer=auctoneer)
        except:
            return self.queryset


class CreateProduct(CreateView):
    model = Product
    form_class = CreateProductForm

    def form_valid(self, form):
        product = form.save(commit=False)
        product.auctoneer = self.request.user
        product.save()
        return redirect('gallery:list')
