from django.urls import path, include
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    
    path('accounts/', include('accounts.urls')),
    
    
]