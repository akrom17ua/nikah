from django.contrib import admin
from .models import ExploreItem

@admin.register(ExploreItem)
class ExploreItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'views', 'likes', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)