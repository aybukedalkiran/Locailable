# Register your models here.
from django.contrib import admin
from .models import Business, BusinessOwner, Availability

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('business_id', 'owner', 'business_name', 'address', 'category', 'phone_number', 'created_at')
    search_fields = ('business_name', 'owner__username')  # Add fields for search functionality

@admin.register(BusinessOwner)
class BusinessOwnerAdmin(admin.ModelAdmin):
    list_display = ('business_owner_id', 'user', 'business', 'created_at')

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('availability_id', 'business', 'available_tables', 'created_at')
    search_fields = ('business__business_name',)
