from django.urls import path
from .views import place_bid,Bids
app_name = 'bid'
urlpatterns = [
   path('place/', place_bid, name='place'),
   path('product/<product>', Bids.as_view(), name = 'product_bids')
]
