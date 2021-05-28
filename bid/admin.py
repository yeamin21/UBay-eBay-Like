import datetime
import json

from django.contrib import admin
# Register your models here.
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count

from bid.models import Bid
from gallery.models import Product


class BidAdmin(admin.ModelAdmin):
    list_display = ("product", "bidder", "created_at", 'bid_ends')
    ordering = ("-created_at",)

    def changelist_view(self, request, extra_context=None):
        now = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
        total_bid = Product.objects.values('created_at__date').annotate(total=Count('id'))
        active_bids = Bid.objects.values('created_at__date').annotate(total=Count('id')).filter(product__ends_at__gt=now)
        print(active_bids)
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(total_bid), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        extra_context['active_bid'] = Bid.objects.filter(product__ends_at__gt=now).count()
        extra_context['active_bids']= json.dumps(list(active_bids), cls=DjangoJSONEncoder)
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    @admin.display(empty_value='unknown')
    def bid_ends(self, obj):
        return obj.product.ends_at


admin.site.register(Bid, BidAdmin)
