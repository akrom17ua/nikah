from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['user_from', 'user_to', 'subject', 'text', 'is_read', 'date']