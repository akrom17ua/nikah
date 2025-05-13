from django.db import models
from django.conf import settings
from user_service.models import UserProfile
from django.core.exceptions import ValidationError

class Message(models.Model):
    user_from = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_to', on_delete=models.CASCADE)
    subject = models.CharField('Message subject', max_length=200, blank = True)
    text = models.TextField('Message text', blank = True, null = True)
    is_read = models.BooleanField('Is read', default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-date'] 
    
    def __str__(self):
        return f'Message from {self.user_from.user.name if self.user_from else "Unknown"} to {self.user_to.name if self.user_to else "Unknown"}'
    
    def clean(self):
        if self.user_from.user == self.user_to:
            raise ValidationError("A user cannot send a message to themselves.")


