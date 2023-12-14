from django.urls import path
from .views import business_detail, place_search

app_name = 'businesses'

urlpatterns = [
    path('business/<int:business_id>/', business_detail, name='business_detail'),
    path('place_search/', place_search, name='place_search')]
