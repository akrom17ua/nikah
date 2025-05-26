
from rest_framework.routers import DefaultRouter
from notification_service.views import MessageListCreateView
from django.urls import path, include



urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name="message-list-create"),  
]