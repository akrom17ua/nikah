from django.db import models


class Interaction(models.Model):
    # user = models.ForeignKey('user_service.UserProfile', on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendor_service.Vendor', on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey('catalog_service.Service', on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=50)  # e.g., 'like', 'follow', etc.
    created_at = models.DateTimeField(auto_now_add=True)