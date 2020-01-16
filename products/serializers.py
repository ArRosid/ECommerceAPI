from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField()

    class Meta:
        model = models.Product
        fields = "__all__"