from django.contrib import admin
from .models import (Stock, Transaction, OfferSale)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('offer', 'quantity', 'active',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('code', 'date', 'state',)


@admin.register(OfferSale)
class OfferSaleAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'offer', 'quantity',)
