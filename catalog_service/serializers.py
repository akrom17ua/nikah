from rest_framework import serializers
from .models import Service, ServiceCategory


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Service
        fields = ['id', 'vendor', 'name', 'description', 'category', 'price', 'image']
        
        
        
class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"