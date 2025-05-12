from rest_framework.routers import DefaultRouter
from catalog_service.views import ServiceViewSet
from django.urls import path, include



catalog_router = DefaultRouter()
catalog_router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(catalog_router.urls)),  
]