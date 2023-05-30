from cafes.views import cafes_view, login
from django.urls import path

urlpatterns = [
    path('', get_login_form),
    path('login', login)
]
