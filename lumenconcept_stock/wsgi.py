import os
from django.core.wsgi import get_wsgi_application
# from stock.tasks import stock_verification, register_transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lumenconcept_stock.settings")

application = get_wsgi_application()

# stock_verification()
# register_transaction()
