from django.db import models
from django.utils import timezone

from gallery.models import Product
from user.models import User


class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True, default=timezone.datetime.now())

    def __str__(self):
        return f'{self.bid_amount} bid on {self.product}'
