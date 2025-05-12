
from django.urls import path, include



from rest_framework.routers import DefaultRouter
from vendor_service.views import VendorViewSet


vendor_router = DefaultRouter()
vendor_router.register(r'vendors', VendorViewSet, basename='vendor')
urlpatterns = [
    path('', include(vendor_router.urls)), 
]