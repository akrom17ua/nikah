from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import WhoAmISerializer
from django.db.models import Q
from drf_yasg.utils  import swagger_auto_schema
from drf_yasg import openapi


from .models import OTP
from .serializers import (
    SendOTPSerializer,
    VerifyOTPSerializer,
    SignUpSerializer,
)

User = get_user_model()
STATIC_OTP = "123456"


class SendOTPView(GenericAPIView):
   
    
    serializer_class   = SendOTPSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes     = [JSONParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        # TODO: integrate real SMS; for now:
        print(f"[DEBUG] Sending static OTP {STATIC_OTP} to {phone_number}")

        return Response({'detail': 'OTP sent.'}, status=status.HTTP_200_OK)


class VerifyOTPView(GenericAPIView):
    
    serializer_class   = VerifyOTPSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes     = [JSONParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        otp   = serializer.validated_data['otp']

        if otp != STATIC_OTP:
            return Response({'detail': 'Invalid OTP.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # get or create user
        user, _ = User.objects.get_or_create(
            phone_number=phone_number,
            defaults={'name': phone_number}
        )

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access':  str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class RefreshTokenView(TokenRefreshView):
    
    permission_classes = [permissions.AllowAny]
    parser_classes     = [JSONParser]


class SignUpView(GenericAPIView):
    
    serializer_class   = SignUpSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes     = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        # partial=True so we only update the fields they send
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    

class WhoAmIView(GenericAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    parser_classes  = [JSONParser]
    serializer_class   = WhoAmISerializer
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="A search term.",
                type=openapi.TYPE_STRING,
                required=False,
            )
        ]
    )
    
    
    
    

    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get('search')
        if search_term:
            # filter across first_name, last_name or phone_number
            qs = User.objects.filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(phone_number__icontains=search_term)
            )
        else:
            # just your user
            qs = User.objects.filter(pk=request.user.pk)

        # always return a list
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)