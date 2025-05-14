from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Service
from rest_framework.parsers import MultiPartParser, FormParser

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, FormParser]