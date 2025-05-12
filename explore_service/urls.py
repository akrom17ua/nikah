from rest_framework.routers import DefaultRouter
from explore_service.views import ExploreItemViewSet
from django.urls import path, include


explore_router = DefaultRouter()
explore_router.register(r'explore', ExploreItemViewSet, basename='explore')

urlpatterns = [
    path('', include(explore_router.urls)),  
]