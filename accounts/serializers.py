
from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'name', 'role', 'is_active', 'date_joined']


class SendOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(min_length=1, max_length=15)

class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(min_length=1, max_length=15)
    otp   = serializers.CharField(min_length=1, max_length=6)

class SignUpSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1)
    
    avatar  = serializers.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('name', 'avatar')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['phone_number'] = user.phone_number
        return token

    def validate(self, attrs):
        # 1) run the base class validation (checks username/password)
        data = super().validate(attrs)

        # 2) append your user info
        data['user'] = {
            'id':       self.user.id,
            'name':     self.user.name,
            'phone':    self.user.phone_number,
            # if you later add avatar URL:
            # 'avatar': getattr(self.user, 'avatar', None) and self.user.avatar.url,
        }
        return data
    
class WhoAmISerializer(serializers.Serializer):
    id           = serializers.UUIDField(read_only=True)
    name   = serializers.CharField(read_only=True, allow_blank=True)
   
    phone_number = serializers.CharField(read_only=True)
    avatar       = serializers.CharField(read_only=True, allow_null=True)