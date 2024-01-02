from django.urls import path
from . import views


urlpatterns = [
    path('', views.business, name='business'),
    path('signup/', views.business_signup, name='business_signup'),
    path('login/', views.business_login, name='business_login'),
    path('logout/', views.business_logout, name='business_logout'),
    path('update/', views.update_business, name='update_business'),
    path('<uuid:business_id>/', views.business_detail, name='business_detail'),
    path('create_availability/<uuid:business_id>/', views.create_availability, name='create_availability'),
    path('create_review/<uuid:business_id>/', views.create_review, name='create_review'),
]