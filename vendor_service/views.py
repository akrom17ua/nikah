from .models import Vendor, VendorImage
from .serializers import VendorSerializer, VendorImageSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class VendorImageViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = VendorImage.objects.all()
    serializer_class = VendorImageSerializer
    
    
    
   
    