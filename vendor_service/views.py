from .models import Vendor, VendorImage
from .serializers import VendorSerializer, VendorImageSerializer, VendorServiceListSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class VendorImageViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = VendorImage.objects.all()
    serializer_class = VendorImageSerializer
    
    
    
   
class VendorListByCategoryView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category_id')
        if not category_id:
            return Response({"detail": "category_id is required"}, status=400)
        vendors = Vendor.objects.filter(services__categroy_id = category_id).distinct()
        serializer = VendorServiceListSerializer(vendors, many = True, context={'category_id': category_id})
        return Response(serializer.data)  
    