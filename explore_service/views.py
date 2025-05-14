from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExploreItemSerializer
from .models import ExploreItem
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser




class ExploreItemViewSet(viewsets.ModelViewSet):
    queryset = ExploreItem.objects.all()
    serializer_class = ExploreItemSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    
    # @action(detail=False, methods=['get'])
    # def popular(self, request):
    #     # Fetch items sorted by likes and views
    #     popular_items = ExploreItem.objects.order_by('-likes', '-views')[:20]  # Top 20 items
    #     serializer = self.get_serializer(popular_items, many=True)
    #     return Response(serializer.data)
    
    # @action(detail=True, methods=['post'])
    # def increment_views(self, request, pk=None):
    #     item = self.get_object()
    #     item.views += 1
    #     item.save()
    #     return Response({'status': 'views incremented', 'views': item.views})
    
    
    # @action(detail=True, methods=['post'])
    # def increment_likes(self, request, pk=None):
    #     item = self.get_object()
    #     item.likes += 1
    #     item.save()
    #     return Response({'status': 'likes incremented', 'likes': item.likes})
    
    
    
    
        