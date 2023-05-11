from cafes.views import cafes_view
from django.urls import path

urlpatterns = [
    path('', cafes_view)
]
