import datetime
import decimal
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
from django.views.generic import DetailView

# from bid.forms import BidForm
from bid.models import Bid
from gallery.models import Product


def place_bid(request):

    bid_product = request.POST.get('bid-product')
    bid_amount = decimal.Decimal(request.POST['bid-amount'])
    now = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
    product = Product.objects.get(pk=bid_product)
    if now <= product.ends_at:
        if bid_amount >= product.minimum_bid_price:
            last_bid = Bid.objects.filter(
                product=product).order_by('-created_at').first()
            if last_bid is not None:
                if bid_amount > last_bid.bid_amount:
                    bid, created = Bid.objects.update_or_create(
                        bidder=request.user, product=product)
                    if not created:
                        bid.bid_amount = bid_amount
                        bid.save()
                        return redirect(to=request.META['HTTP_REFERER']+'?status=added')
                    else:
                        bid.bid_amount = bid_amount
                        bid.save()

                else:
                    return HttpResponse('<h1>Bid has to be more than the last bid</h1>')
            else:
                bid, created = Bid.objects.update_or_create(
                    bidder=request.user, product=product)
                if not created:
                    bid.bid_amount = bid_amount
                    bid.save()
                    return redirect(to=request.META['HTTP_REFERER']+'?status=updated')
                else:
                    bid.bid_amount = bid_amount
                    bid.save()

            return redirect(to=request.META['HTTP_REFERER']+'?status=added')
        else:
            return HttpResponse('<h1>Amount is less than starting price</h1>')
    else:
        return HttpResponse('<h1>Time Expired</h1>')
    return redirect('gallery:list')


class Bids(DetailView):
    model = Bid
    template_name = 'gallery/product_detail.html'
    context_object_name = 'bids'

# class PlaceBid(CreateView):
#     model = Bid
#     fields = ['bidder','bid_amount','product']
#     # form_class = BidForm
#
#     def form_valid(self, form):
#         p = self.request.POST.get('bid-product')
#         q = self.request.POST.get('bid-amount')
#         print(p,q)
