from django.urls import path
from .views import (
    SendOTPView,
    VerifyOTPView,
    RefreshTokenView,
    SignUpView,
    WhoAmIView,
)

urlpatterns = [
    path('auth/send-otp/',      SendOTPView.as_view(),    name='auth_send_otp'),
    path('auth/verify-otp/',    VerifyOTPView.as_view(),  name='auth_verify_otp'),
    path('auth/refresh-token/', RefreshTokenView.as_view(), name='auth_refresh_token'),
    path('auth/sign-up/',       SignUpView.as_view(),     name='auth_sign_up'),
    path('auth/whoami/',        WhoAmIView.as_view(),      name='auth_whoami'),
]
