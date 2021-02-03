from django.contrib import admin
from .models import Product, Category, Manufacturer, Buyer, Order, Supply

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Buyer)
admin.site.register(Order)
admin.site.register(Supply)