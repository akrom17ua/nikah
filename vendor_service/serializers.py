from rest_framework import serializers
from .models import Vendor, VendorImage

class VendorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorImage
        fields = ['id', 'image', 'uploaded_at']


class VendorSerializer(serializers.ModelSerializer):
    
    images = VendorImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    class Meta:
        model = Vendor
        fields = ['id', 'business_name', 'description', 'address', 'phone_number', 'email', 'images', 'created_at', 'uploaded_images']
        
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        vendor = Vendor.objects.create(**validated_data)

        for image in uploaded_images:
            VendorImage.objects.create(vendor=vendor, image=image)
        
        return vendor