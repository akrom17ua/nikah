from django.db import models
from vendor_service.models import Vendor
from django.conf import settings

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    vendor = models.ForeignKey('vendor_service.Vendor', on_delete=models.CASCADE, related_name='services')
    category = models.ForeignKey('catalog_service.ServiceCategory', on_delete=models.SET_NULL, null = True, related_name='catalog_services')  
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/service/', null=True, blank=True)
    available = models.BooleanField(default=True, blank = True)

    def __str__(self):
        return f"{self.name} by {self.vendor.business_name}"


class SavedService(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "saved_services")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="saved_by")
    saved_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        unique_together = ('user', 'service')