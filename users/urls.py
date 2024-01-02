from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    #path('profile/<uuid:owner_id>/', views.userProfile, name='user_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('add_review/', views.add_review, name='add_review'),
    #path('vote_review/<int:review_id>/<str:value>/', views.vote_review, name='vote_review'),
]