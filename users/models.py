from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    user_groups = models.ManyToManyField(Group, related_name='users', blank=True, help_text='The groups this user belongs to.')
    user_permissions = models.ManyToManyField(Permission, related_name='users', blank=True, help_text='Specific permissions for this user.')

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created_at']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except ValueError:
            url = ''
        return url
