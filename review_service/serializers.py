from rest_framework import serializers
from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'vendor', 'service', 'rating', 'comment', 'created_at']
