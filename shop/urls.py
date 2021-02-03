from django.conf.urls import url, include
from .views import ProductViewset, OrderViewset, SupplyViewset, CategoryViewset, BuyerViewset, ManufacturerViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewset, basename='product')
router.register('order', OrderViewset, basename='order')
router.register('supply', SupplyViewset, basename='supply')
router.register('manufacturer', ManufacturerViewset, basename='manufacturer')
router.register('category', CategoryViewset, basename='category')
router.register('buyer', BuyerViewset, basename='buyer')

urlpatterns = [
    url('', include(router.urls)),


]