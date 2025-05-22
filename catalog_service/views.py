from rest_framework import viewsets
from .serializers import ServiceSerializer, ServiceCategorySerializer
from .models import Service, ServiceCategory
from rest_framework.parsers import MultiPartParser, FormParser

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    
class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    parser_classes = [MultiPartParser, FormParser]