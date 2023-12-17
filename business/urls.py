from django.urls import path
from .views import business_detail, business_search

app_name = 'businesses'

urlpatterns = [
    path('business/<int:business_id>/', business_detail, name='business_detail'),
    path('business_search/', business_search, name='business_search')
]
