from rest_framework import serializers
from .models import CustomUser, OTP



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'name', 'role', 'is_active', 'date_joined']


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['id', 'phone_number', 'code', 'created_at', 'is_used']