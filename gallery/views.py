from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView

from bid.models import Bid
from gallery.forms import CreateProductForm
from gallery.models import Product
from user.models import User


class ProductList(LoginRequiredMixin, ListView):
    login_url = '/auth/login'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        user = self.kwargs.get('user')
        if user is not None:
            auctoneer = User.objects.get(email=self.kwargs['user'])
            return self.model.objects.filter(auctoneer=auctoneer)
        else:
            return Product.objects.all()


class ProductDetails(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bids = Bid.objects.filter(product=self.kwargs['pk']).order_by('-bid_amount')
        last_bid = bids.first()
        if last_bid:
            context['last_bid'] = last_bid
        context['bids'] = bids
        return context


class CreateProduct(CreateView):
    model = Product
    form_class = CreateProductForm

    def form_valid(self, form):
        product = form.save(commit=False)
        product.auctoneer = self.request.user
        product.save()

        return redirect('gallery:list')
