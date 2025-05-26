from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated


class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self, request):
        user = self.request.user
        service_id = request.query_params.get('service')
        qs = Message.objects.filter(receiver=user) | Message.objects.filter(sender__user = user)
        if service_id:
            qs = qs.filter(service_id=service_id)
        return qs.order_by('-date')
    
    
    def perform_create(self, serializer):
        sender_profile = self.request.user
        serializer.save(sender=sender_profile)
    