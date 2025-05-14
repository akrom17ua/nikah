from django.urls import path, include
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('check/', views.check, name='check'),
    path('accounts/', include('accounts.urls')),
    path('vendor/', include('vendor_service.urls')),
    path('user/', include('user_service.urls')),
    path('catalog/', include('catalog_service.urls')),
    path('explore/', include('explore_service.urls')),
    path('interaction/', include('interaction_service.urls')),
    path('review/', include('review_service.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]