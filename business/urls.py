from django.urls import path
from .views import business_detail

app_name = 'businesses'

urlpatterns = [
    path('business/<int:business_id>/', business_detail, name='business_detail'),
    # Add more paths as needed
]
