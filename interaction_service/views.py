from django.shortcuts import render
from rest_framework import viewsets
from .models import Interaction
from .serializers import InteractionSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer