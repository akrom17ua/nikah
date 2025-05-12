from django.db import models

# Create your models here.
# class Message(models.Model):
#     user_from = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_to = models.ForeignKey(User, related_name='user_to', on_delete=models.CASCADE)
#     subject = models.CharField('Message subject', max_length=200)
#     text = models.TextField('Message text')
#     is_read = models.BooleanField('Is read', default=False)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Message from {self.user_from} to {self.user_to}'