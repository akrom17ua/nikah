from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from user_service.models import UserProfile
from vendor_service.models import Vendor

@receiver(post_save, sender=CustomUser)
def create_user_profile_and_vendor(sender, instance, created, **kwargs):
    if created:
        # Create a UserProfile for every user
        UserProfile.objects.create(user=instance)

        # If the user is a vendor, create a Vendor profile
        if instance.role == 'vendor':  # Assuming you added a 'role' field to CustomUser
            Vendor.objects.create(owner=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.client_profile.save()