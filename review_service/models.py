from django.db import models

# Create your models here.
class Review(models.Model):
    # author = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='reviews')
    # user = models.ForeignKey('user_service.UserProfile', on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendor_service.Vendor', on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey('catalog_service.Service', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(default=1)  # 1-5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     unique_together = ('author', 'vendor')
    #     ordering = ['-created_at']

    # def __str__(self):
    #     return f"Review by {self.author.user.username} for {self.vendor.business_name}"