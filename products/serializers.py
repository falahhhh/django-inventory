from rest_framework import serializers
from .models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'product']