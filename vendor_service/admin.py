from django.contrib import admin
from .models import Vendor, VendorImage

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'phone_number', 'created_at')
    search_fields = ('business_name',)

@admin.register(VendorImage)
class VendorImageAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'uploaded_at')
    search_fields = ('vendor__business_name',)
    filter_horizontal = ('categories',) 