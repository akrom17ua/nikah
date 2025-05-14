from .models import Vendor
from .serializers import VendorSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)