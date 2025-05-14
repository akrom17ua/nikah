# accounts/views.py
import random
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OTP, CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class SendOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        if not phone:
            return Response({'error': 'phone_number is required'}, status=400)
        code = str(random.randint(10000, 99999))
        OTP.objects.create(phone_number=phone, code=code)
        return Response({'otp': code, 'message': 'OTP sent'})
    
    
    
class VerifyOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        code = request.data.get('code')
        otp = OTP.objects.filter(phone_number=phone, code=code, is_used=False).order_by('-created_at').first()
        if otp and otp.is_valid():
            otp.is_used = True
            otp.save()
            user, created = CustomUser.objects.get_or_create(phone_number=phone, defaults={'name': phone})
            
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            })
        return Response({'error': 'Invalid or expired OTP'}, status=400)