
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from review_service.views import ReviewViewSet


review_router = DefaultRouter()
review_router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(review_router.urls)), 
]