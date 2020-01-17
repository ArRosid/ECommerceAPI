from rest_framework import generics, viewsets

from core import utils

from . import models, serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = utils.SmallResultPagination

class ProductFeaturedList(generics.ListAPIView):
    queryset = models.Product.objects.featured()
    serializer_class = serializers.ProductSerializer
    pagination_class = utils.SmallResultPagination

class ProductActiveList(generics.ListAPIView):
    queryset = models.Product.objects.active()
    serializer_class = serializers.ProductSerializer
    pagination_class = utils.SmallResultPagination