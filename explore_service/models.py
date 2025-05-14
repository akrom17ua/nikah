from django.db import models
from catalog_service.models import ServiceCategory

class ExploreItem(models.Model):
    category = models.ForeignKey('catalog_service.ServiceCategory', on_delete=models.SET_NULL, null=True, blank = True, related_name='explore_items') 
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name