
from rest_framework.routers import DefaultRouter
from notification_service.views import MesssageViewSet
from django.urls import path, include

notification_router = DefaultRouter()
notification_router.register(r'notifications', MesssageViewSet, basename='notification')


urlpatterns = [
    path('', include(notification_router.urls)),  
]