from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.business, name='business'),
    path('<int:business_id>/', views.business_detail, name='business_detail'),
    path('create/', views.create_business, name='create_business'),
    path('update/<int:business_id>/', views.update_business, name='update_business'),
    path('delete/<int:business_id>/', views.delete_business, name='delete_business'),
    path('availability/<int:business_id>/', views.create_availability, name='create_availability'),
    path('review/<int:business_id>/', views.create_review, name='create_review'),
    path('check_in_out/<int:business_id>/', views.check_in_out, name='check_in_out'),
]
