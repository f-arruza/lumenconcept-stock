import requests, decimal

from rest_framework import serializers

from django.conf import settings
from django.db import DatabaseError, transaction

from .models import (Stock, Transaction, OfferSale)
from .utils import send_message_rabbit


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class OfferSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfferSale
        fields = '__all__'
