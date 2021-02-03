from .models import Product, Order, Supply, Buyer, Manufacturer, Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'specifications', 'manufacturer', 'price', 'supply']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'number', 'product', 'buyer', 'date']


class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ['id', 'number', 'date']


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = ['id', 'name', 'number']


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['id', 'manufacturer']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']


