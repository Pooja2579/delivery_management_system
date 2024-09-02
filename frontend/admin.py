from django.contrib import admin
from .models import Parcel, StatusUpdate, Profile

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('parcel_id', 'receiver_name', 'status', 'created_at')
    search_fields = ('parcel_id', 'receiver_name', 'sender_name')
    list_filter = ('status', 'created_at')

@admin.register(StatusUpdate)
class StatusUpdateAdmin(admin.ModelAdmin):
    list_display = ('parcel', 'status', 'location', 'update_time')
    search_fields = ('parcel__parcel_id', 'location')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
