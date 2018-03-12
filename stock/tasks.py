import json, pika
from django.conf import settings
from .models import (Stock, Transaction, OfferSale)
from .utils import send_message_rabbit, receive_message_rabbit
from background_task import background

@background(schedule=1)
def stock_verification():

    def callback(ch, method, properties, body):
        payload = json.loads(body.decode('utf-8'))
        try:
            order_code = payload['order_code']
            offers = payload['offers']
            success = "true"
            details = []

            if len(offers)==0:
                detail = {
                    "code": "0",
                    "error": "BAD_REQUEST"
                }
                success = "false"
                details.append(detail)
            else:
                for offer in offers:
                    rs = Stock.objects.filter(offer=offer['code'],
                                              quantity__gt=offer['quantity'],
                                              active=True)
                    if len(rs)==0:
                        detail = {
                            "code": offer['code'],
                            "error": "NOT_AVAIBLE"
                        }
                        success = "false"
                        details.append(detail)
            response = {
                "order_code": order_code,
                "success": success,
                "details": details
            }
            # Enviar resultado de verificación a ORDER SERVICE
            send_message_rabbit('stock.verification.response', response)
        except:
            print('ERROR')

    receive_message_rabbit('stock.verification.request', callback)


@background(schedule=1)
def register_transaction():

    def callback(ch, method, properties, body):
        payload = json.loads(body.decode('utf-8'))
        # try:
        sale_code = payload['sale_code']
        offers = payload['offers']
        success = "true"
        details = []

        if len(offers)==0:
            detail = {
                "code": "0",
                "error": "BAD_REQUEST"
            }
            success = "false"
            details.append(detail)
        else:
            for offer in offers:
                rs = Stock.objects.filter(offer=offer['code'],
                                          quantity__gt=offer['quantity'],
                                          active=True)
                if len(rs)==0:
                    detail = {
                        "code": offer['code'],
                        "error": "NOT_AVAIBLE"
                    }
                    success = "false"
                    details.append(detail)

        if success == "true":
            # Registrar Transaction
            print('Registrar Transaction')
            transaction = Transaction(code=sale_code)
            transaction.save()

            for offer in offers:
                # Hacer la descarga del stock
                stock = Stock.objects.get(offer=offer['code'])
                qt = stock.quantity - int(offer['quantity'])
                print(qt)
                stock.quantity = qt
                stock.save()
                print(stock.quantity)

                # Registrar OfferSale
                ofs = OfferSale(transaction=transaction,
                                offer=offer['code'],
                                quantity=int(offer['quantity']))
                ofs.save()

        response = {
            "sale_code": sale_code,
            "success": success,
            "details": details
        }
        # Enviar resultado de transaction
        send_message_rabbit('stock.transaction.response', response)
        # except:
        #     print('ERROR')

    receive_message_rabbit('stock.transaction.request', callback)
