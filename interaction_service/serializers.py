from rest_framework import serializers
from .models import Interaction


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'user', 'vendor', 'product', 'action', 'created_at']