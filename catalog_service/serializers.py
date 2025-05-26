from rest_framework import serializers
from .models import Service, ServiceCategory, SavedService
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Service
        fields = ['id', 'vendor', 'name', 'description', 'category', 'price', 'image']
        
        
        
class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"
        
        
class SavedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedService
        fields = "__all__"
        
        
