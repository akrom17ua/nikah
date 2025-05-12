from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExploreItemSerializer
from .models import ExploreItem


class ExploreItemViewSet(viewsets.ModelViewSet):
    queryset = ExploreItem.objects.all()
    serializer_class = ExploreItemSerializer