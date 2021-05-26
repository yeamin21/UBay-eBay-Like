from django.forms import ModelForm

from bid.models import Bid


class BidForm(ModelForm):
    def __init__(self, *args, **kwargs):

        bidder = kwargs.pop('bidder')
        product = kwargs.pop('product')
        bid_amount = kwargs.pop('bid_amount')
        self.bidder = bidder
        self.product = product
        self.bid_amount = bid_amount
        super().__init__(*args, **kwargs)

    class Meta:
        model = Bid
        #fields = '__all__'
        exclude = ['bidder']

    # def save(self, commit=True ):
    #     bid = super().save(commit=False)
    #     bid = Bid.objects.update_or_create(product=self.product, bidder = self.bidder)
    #     bid.bid_amount = self.bid_amount
    #     bid.save(commit=True)
    #     return bid
