from django.db import models
from django.conf import settings




class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_profile')
    bio = models.TextField(blank=True)
    wedding_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    

    def __str__(self):
        return self.user.name