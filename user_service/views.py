from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer

from rest_framework.parsers import MultiPartParser, FormParser


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = [MultiPartParser, FormParser]