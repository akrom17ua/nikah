from rest_framework import serializers
from .models import ExploreItem



class ExploreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExploreItem
        fields = ['id', 'name', 'description', 'category', 'image', 'created_at']