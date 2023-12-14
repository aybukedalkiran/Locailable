# Register your models here.
from django.contrib import admin
from .models import Review, Reservation, VisitedPlaces

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'user', 'business', 'rating', 'created_at')
    search_fields = ('user__username', 'business__business_name')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'user', 'business', 'date', 'time', 'group_size', 'created_at')
    search_fields = ('user__username', 'business__business_name')


@admin.register(VisitedPlaces)
class VisitedPlacesAdmin(admin.ModelAdmin):
    list_display = ('visit_id', 'user', 'business', 'created_at')
    search_fields = ('user__username', 'business__business_name')
