from django.contrib import admin
from .models import MarketPrice,Person, Pending_Buy_Order, Pending_Sell_Order, Transaction

admin.site.register(Pending_Sell_Order)
admin.site.register(Transaction)
admin.site.register(Pending_Buy_Order)
admin.site.register(Person)
admin.site.register(MarketPrice)
