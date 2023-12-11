from django.urls import path
from .views import review_detail

app_name = 'reviews'

urlpatterns = [
    path('review/<int:review_id>/', review_detail, name='review_detail'),
    # Add more paths as needed
]