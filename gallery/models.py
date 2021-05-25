from django.db import models
from user.models import User


class Product(models.Model):
    # Product Name, Product Description, Product Photo, Minimum Bid Price, and Auction End DateTime
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='product/')
    minimum_bid_price = models.DecimalField(decimal_places=2, max_digits=7)
    ends_at = models.DateTimeField()
    auctoneer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
