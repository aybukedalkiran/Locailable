from django.urls import path
from .views import user_detail

app_name = 'users'

urlpatterns = [
    path('user/<int:user_id>/', user_detail, name='user_detail'),
    # Add more paths as needed
]
