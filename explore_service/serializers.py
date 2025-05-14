from rest_framework import serializers
from .models import ExploreItem




class ExploreItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = ExploreItem
        fields = '__all__'