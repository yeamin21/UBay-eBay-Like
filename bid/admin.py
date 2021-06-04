import datetime
import json

from django.contrib import admin
# Register your models here.
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Max, Sum

from bid.models import Bid
from gallery.models import Product


class BidAdmin(admin.ModelAdmin):
    list_display = ("product", "bidder", "created_at", 'bid_ends')
    ordering = ("-created_at",)
    change_list_template = 'admin/bid/Bid/change_list.html'

    def changelist_view(self, request, extra_context=None):
        now = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
        all_bid = Product.objects.values(
            'created_at__date').annotate(count=Count('id'))
        q = Bid.objects.values('created_at__date', 'product').filter(product__ends_at__gt=now)\
            .annotate(count=Count('bid_amount'))

        # .aggregate(count=Count('max'))
        active_bids = q
        extra_context = extra_context or {}
        extra_context['all_bid'] = json.dumps(
            list(all_bid), cls=DjangoJSONEncoder)
        extra_context['no_active_bid'] = Bid.objects.filter(
            product__ends_at__gt=now).count()
        extra_context['active_bids'] = json.dumps(
            list(active_bids), cls=DjangoJSONEncoder)
        max_bids = Bid.objects.values('product').filter(
            product__ends_at__gt=now).annotate(max_bid=Max('bid_amount'))
        extra_context['active_bid_total'] = max_bids.aggregate(Sum('max_bid'))

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    @admin.display(empty_value='unknown')
    def bid_ends(self, obj):
        return obj.product.ends_at


admin.site.register(Bid, BidAdmin)
