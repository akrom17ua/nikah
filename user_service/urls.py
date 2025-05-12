from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_service.views import UserProfileViewSet


user_router = DefaultRouter()
user_router.register(r'profiles', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('', include(user_router.urls)),
]
