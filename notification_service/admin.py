from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'subject', 'is_read', 'date')
    search_fields = ('user_from__user__name', 'user_to__name', 'subject')
    list_filter = ('is_read', 'date')