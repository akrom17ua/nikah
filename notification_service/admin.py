from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'is_read', 'date')
    search_fields = ('sender__user__name', 'receiver__name', 'subject')
    list_filter = ('is_read', 'date')