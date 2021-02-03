from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductSerializer, OrderSerializer, SupplySerializer, BuyerSerializer, ManufacturerSerializer, CategorySerializer
from .models import Product, Order, Supply, Buyer, Manufacturer, Category


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order = Order.objects.all()
        return order


class SupplyViewset(viewsets.ModelViewSet):
    serializer_class = SupplySerializer

    def get_queryset(self):
        supply = Supply.objects.all()
        return supply


class BuyerViewset(viewsets.ModelViewSet):
    serializer_class = BuyerSerializer

    def get_queryset(self):
        buyer = Buyer.objects.all()
        return buyer


class ManufacturerViewset(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        manufacturer = Manufacturer.objects.all()
        return manufacturer


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category