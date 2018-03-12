from django.conf.urls import url, include

from .views import (schema_view, StockViewSet, TransactionViewSet,
                    OfferSaleViewSet, CleanView)

api_url_patterns = [
    url(r'^stocks/$', StockViewSet.as_view({
                                           'get': 'list',
                                           'post': 'create',
                                           }), name='stocks-list'),
    url(r'^stocks/(?P<pk>[0-9]+)$', StockViewSet.as_view({
                                                   'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'
                                                  }), name='stocks'),
    url(r'^transactions/$', TransactionViewSet.as_view({
                                                   'get': 'list',
                                                   'post': 'create',
                                                  }), name='transaction-list'),
    url(r'^transactions/(?P<pk>[0-9]+)$', TransactionViewSet.as_view({
                                                   'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'
                                                  }), name='transaction'),
    url(r'^offersales/$', OfferSaleViewSet.as_view({
                                       'get': 'list',
                                       'post': 'create',
                                       }), name='offersale-list'),
    url(r'^offersales/(?P<pk>[0-9]+)$', OfferSaleViewSet.as_view({
                                                     'get': 'retrieve',
                                                     'put': 'update',
                                                     'patch': 'partial_update',
                                                     'delete': 'destroy'
                                                    }), name='offersale'),
]

urlpatterns = [
    url(r'^api/v1/', include(api_url_patterns)),
    url(r'^cleaner/$', CleanView.as_view(), name='cleaner'),
    url(r'^', schema_view),    
]
