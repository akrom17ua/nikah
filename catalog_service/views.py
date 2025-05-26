from rest_framework import viewsets
from .serializers import ServiceSerializer, ServiceCategorySerializer
from .models import Service, ServiceCategory
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    
class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    parser_classes = [MultiPartParser, FormParser]
    

class VenuesNearYouView(APIView):
    def get(self, request):
        region = request.query_params.get('region')
        service_type = request.query_params.get('service_type')
        if not region or not service_type:
            return Response({"detail": "Region and service_type is required"}, status = 400)
        venues = Service.objects.filter(location__iexact = region, category__name__iexact = service_type)
        serializer = ServiceSerializer(venues, many = True)
        return Response(serializer.data)
    
    
class SellersNearYouView(APIView):
    def get(self, request):
        region = request.query_params.get("region")
        service_type = request.query_params.get("service_type")
        if not region or not service_type:
            return Response({"detail": "Region and service_type are required"}, status = 400)
        sellers = Service.objects.filter(location__iexact = region, category__name__iexact = service_type )
        serializer = ServiceSerializer(sellers, many = True)
        return Response(serializer.data)