from rest_framework.routers import DefaultRouter
from catalog_service.views import ServiceViewSet, ServiceCategoryViewSet, VenuesNearYouView, SellersNearYouView
from django.urls import path, include



service_router = DefaultRouter()
service_router.register(r'services', ServiceViewSet, basename='service')


catalog_router = DefaultRouter()
catalog_router.register(r"categories", ServiceCategoryViewSet, basename="categories")

urlpatterns = [
    path('', include(service_router.urls)),  
    path('', include(catalog_router.urls)),
    path('/venues/near-you/', VenuesNearYouView.as_view(), name = "near-you-venues"),
    path('/sellers/near-you/', SellersNearYouView.as_view(), name="sellers-near-you"),
]