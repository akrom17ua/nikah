from django.db import models
from vendor_service.models import Vendor

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
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/service/', null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} by {self.vendor.business_name}"



