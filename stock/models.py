from django.db import models


class Stock(models.Model):
    offer = models.CharField('Code', max_length=36)
    quantity = models.PositiveIntegerField('Quantity', default=0)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.offer + ": " + str(self.quantity)

    class Meta:
        db_table = 'stock'
        verbose_name_plural = 'Stocks'


class Transaction(models.Model):
    code = models.CharField('Code', max_length=36)
    date = models.DateTimeField(auto_now=True)
    STATES = (
        ('01', 'SUCCESS'),
        ('02', 'REJECT'),
    )
    state = models.CharField('State', max_length=2, choices=STATES,
                              default='01')

    def __str__(self):
        return self.code + ": " + str(self.date)

    class Meta:
        db_table = 'transaction'
        verbose_name_plural = 'Transactions'


class OfferSale(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE,
                                    related_name='offers')
    offer = models.CharField('Offer', max_length=36)
    quantity = models.PositiveIntegerField('Quantity', default=0)

    def __str__(self):
        return self.offer + ": " + str(self.quantity)

    class Meta:
        db_table = 'offer_sale'
        verbose_name_plural = 'OfferSales'
