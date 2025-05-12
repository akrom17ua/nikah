
from rest_framework.routers import DefaultRouter
from interaction_service.views import InteractionViewSet
from django.urls import path, include

interaction_router = DefaultRouter()
interaction_router.register(r'interactions', InteractionViewSet, basename='interaction')


urlpatterns = [
    path('', include(interaction_router.urls)),  
]