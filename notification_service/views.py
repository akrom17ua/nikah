from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated


class MesssageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
