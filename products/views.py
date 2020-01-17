from rest_framework import viewsets, generics

from . import models
from . import serializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductFeaturedList(generics.ListAPIView):
    queryset = models.Product.objects.featured()
    serializer_class = serializers.ProductSerializer

class ProductActiveList(generics.ListAPIView):
    queryset = models.Product.objects.active()
    serializer_class = serializers.ProductSerializer