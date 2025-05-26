from .views import VendorListByCategoryView
from django.urls import path, include



from rest_framework.routers import DefaultRouter
from vendor_service.views import VendorViewSet, VendorImageViewSet



vendor_router = DefaultRouter()
vendor_router.register(r'vendors', VendorViewSet, basename='vendor')

vendor_image_router = DefaultRouter()
vendor_image_router.register(r'vendor-images', VendorImageViewSet, basename="vendor-images")

urlpatterns = [
    path('', include(vendor_router.urls)), 
    path('', include(vendor_image_router.urls)),
    path('vendors-by-category/', VendorListByCategoryView.as_view(), name='vendors-by-category'),
]