from django.db import models
from django.conf import settings
from user_service.models import UserProfile
from django.core.exceptions import ValidationError
from catalog_service.models import Service

class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_to', on_delete=models.CASCADE)
    subject = models.CharField('Message subject', max_length=200, blank = True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField('Message text', blank = True, null = True)
    is_read = models.BooleanField('Is read', default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-date'] 
    
    def __str__(self):
        return f'Message from {self.sender.user.name if self.sender else "Unknown"} to {self.receiver.name if self.receiver else "Unknown"}'
    
    def clean(self):
        if self.sender.user == self.receiver:
            raise ValidationError("A user cannot send a message to themselves.")


