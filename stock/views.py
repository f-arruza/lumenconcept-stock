from stock import urls

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import response, schemas
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes

from .models import (Stock, Transaction, OfferSale)
from .serializers import (StockSerializer, TransactionSerializer, OfferSaleSerializer)


@api_view()
@permission_classes((AllowAny, ))
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='LumenConcept Stock API Docs',
                                        patterns=urls.api_url_patterns,
                                        url='/api/v1/')
    return response.Response(generator.get_schema())


class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.filter(active=True)

    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'offer',
    )


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'code', 'state',
    )


class OfferSaleViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSaleSerializer
    queryset = OfferSale.objects.all()

    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'offer',
    )
