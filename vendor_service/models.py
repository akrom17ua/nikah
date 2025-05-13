from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class Vendor(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor_profile', null=True, blank=True)
    business_name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null = True, blank = True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name
    
class VendorImage(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vendor_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vendor.name} - Image {self.id}"