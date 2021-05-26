import datetime

from django.db import models
from user.models import User



class Product(models.Model):
    # Product Name, Product Description, Product Photo, Minimum Bid Price, and Auction End DateTime
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='product/')
    minimum_bid_price = models.DecimalField(decimal_places=2, max_digits=9)
    ends_at = models.DateTimeField()
    auctoneer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_expired = models.BooleanField(default=False)

    @property
    def is_expired(self):
        if datetime.datetime.now().replace(tzinfo=datetime.timezone.utc) > self.ends_at:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.name}'
