from rest_framework import serializers
from .models import Vendor, VendorImage
from review_service.models import Review
from django.db.models import Avg



class VendorImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = VendorImage
        fields = '__all__'

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
    
    
class VendorServiceListSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Vendor
        fields = ['id', 'business_name', 'address', 'services', 'min_price', 'average_rating']
        
    def get_services(self, obj):
        category_id = self.context.get('category_id')
        return list(obj.services.filter(category_id=category_id).values_list('name', flat=True))
                    
    def get_min_price(self, obj):
        category_id = self.context.get('category_id')
        prices = obj.services.filter(category_id = category_id).values_list('price', flat=True)
        
    def get_average_rating(self, obj):
        category_id = self.context.get('category_id')
        # Get all services for this vendor in the selected category
        service_ids = obj.services.filter(category_id=category_id).values_list('id', flat=True)
        # Get all reviews for these services
        reviews = Review.objects.filter(service_id__in=service_ids)
        avg = reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 2) if avg else None
    
    def get_review_count(self, obj):
        category_id = self.context.get('category_id')
        service_ids = obj.services.filter(category_id=category_id).values_list('id', flat=True)
        return Review.objects.filter(service_id__in=service_ids).count()
