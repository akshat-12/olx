from django.db.models import fields
from rest_framework import serializers
from products.models import Product, Owner, Image

class ProductSerializer(serializers.ModelSerializer):
    Images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = "__all__"

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"