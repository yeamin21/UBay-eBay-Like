from django.forms import ModelForm

from bid.models import Bid


class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['bidder']
