from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignupForm, UserProfileForm

User = get_user_model()

def home(request):
    return render(request, 'users/home.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User account was created!')
            return redirect('users:home')
        else:
            # Print form errors to console for debugging
            print(form.errors)
    else:
        form = UserSignupForm()

    return render(request, 'users/user_signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('users:home')  # Redirect to home on successful login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/user_login.html')
def user_logout(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('users:home')

@login_required
def user_profile(request):
    return render(request, 'users/user_profile.html')

@login_required
def update_profile(request):
    return render(request, 'users/update_profile.html')

@login_required
def delete_profile(request):
    return render(request, 'users/delete_profile.html')
