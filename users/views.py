from django.shortcuts import render
from .models import User

def user_detail(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    return render(request, 'users/user_detail.html', {'user': user})
# Create your views here.
