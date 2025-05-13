from django.contrib import admin
from .models import Vendor, VendorImage, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(VendorImage)
class VendorImageAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'uploaded_at')
    search_fields = ('vendor__business_name',)
    filter_horizontal = ('categories',) 