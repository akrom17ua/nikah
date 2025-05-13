from django.urls import path, include
from api import views


urlpatterns = [
    path('check/', views.check, name='check'),
    # path('auth/', include('auth_service.urls')),
    path('vendor/', include('vendor_service.urls')),
    path('user/', include('user_service.urls')),
    path('catalog/', include('catalog_service.urls')),
    path('explore/', include('explore_service.urls')),
    path('interaction/', include('interaction_service.urls')),
    path('review/', include('review_service.urls')),
    
]