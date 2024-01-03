from django.contrib import admin

# Register your models here.
from .models import Business, Availability, Review

admin.site.register(Business)
admin.site.register(Availability)
admin.site.register(Review)