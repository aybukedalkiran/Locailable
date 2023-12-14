# Register your models here.
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'last_name', 'username', 'email', 'phone', 'created_at')
    search_fields = ('name', 'last_name', 'username', 'email')

    # Optional: Customize the fields displayed when editing a single user
    fields = ('name', 'last_name', 'username', 'email', 'password', 'phone', 'created_at')
    readonly_fields = ('created_at',)  # Make 'created_at' field read-only

    # Optional: Customize the ordering of users in the admin list view
    ordering = ('-created_at',)
