from django.db import models

class Review(models.Model):
    user = models.ForeignKey('user_service.UserProfile', on_delete=models.CASCADE, related_name='reviews', null = True)
    vendor = models.ForeignKey('vendor_service.Vendor', on_delete=models.CASCADE, related_name='reviews')
    service = models.ForeignKey('catalog_service.Service', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1)  
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'service')
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user} for {self.service} (Vendor: {self.vendor})"