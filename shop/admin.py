from django.contrib import admin
from .models import Product, Category, Manufacturer, Buyer, Order, Supply
from import_export.admin import ImportExportModelAdmin

def in_progress(modeladmin, request, queryset):
    queryset.update(status='В процессе')
in_progress.short_description = "Изменить статус заказа 'В процессе'"

def completed(modeladmin, request, queryset):
    queryset.update(status='Выполнен')
completed.short_description = "Изменить статус заказа 'Выполнен'"

def canceled(modeladmin, request, queryset):
    queryset.update(status='Отменен')
canceled.short_description = "Изменить статус заказа 'Отменен'"

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'specifications', 'manufacturer', 'price', 'supply')
    list_display_links = ('title', 'manufacturer')
    list_filter = ('category', 'manufacturer')
    search_fields = ("title__startswith", )
    pass


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('title', )
    search_fields = ("title__startswith", )
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(ImportExportModelAdmin):
    list_display = ('manufacturer', )
    search_fields = ("manufacturer__startswith", )
    pass


@admin.register(Buyer)
class BuyerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'number')
    search_fields = ("name__startswith",)
    pass


@admin.register(Supply)
class SupplyAdmin(ImportExportModelAdmin):
    list_display = ('number', 'date')
    search_fields = ("name__startswith",)
    pass

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('number', 'product', 'buyer', 'date', 'status')
    search_fields = ("name__startswith",)
    actions = [in_progress, completed, canceled]
    pass


