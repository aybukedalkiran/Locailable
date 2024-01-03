from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserSignupForm, UserProfileForm
from business.forms import ReviewForm
#from .forms import UserSignupForm, UserProfileForm, UserReviewForm
#from .models import UserVote, UserReview
from business.models import Review


def home(request):
    return render(request, 'users/home.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'users/user_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        #username = request.POST['username'].lower()
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/user_login.html')


def user_logout(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('home')  # Assuming you have a 'home' URL pattern
    #return redirect('login')


@login_required
def user_profile(request):
    reviews = Review.objects.filter(owner=request.user.profile)
    return render(request, 'users/user_profile.html', {'reviews': reviews})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user.profile)

    context = {'form': form}
    return render(request, 'users/update_profile.html', context)


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')

    return render(request, 'users/delete_profile.html')


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('user_profile')
    else:
        form = ReviewForm()
    return render(request, 'users/add_review.html', {'form': form})

"""
@login_required
def vote_review(request, review_id, value):
    review = ReviewForm.objects.get(id=review_id)

    # Kullanıcının bu review'a daha önce oy verip vermediğini kontrol etmek için
    existing_vote = UserVote.objects.filter(user=request.user, review=review).first()

    if existing_vote:
        # Kullanıcı zaten oy vermiş, oyunu güncelle
        existing_vote.value = value
        existing_vote.save()
    else:
        # Kullanıcı ilk kez oy veriyor
        vote = UserVote(user=request.user, review=review, value=value)
        vote.save()

    return redirect('user_profile')
"""













"""
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('user_account')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'user_account'))

        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')
"""


"""
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserSignupForm(instance=request.user.profile)
    return render(request, 'users/update_profile.html', {'form': form})
"""

"""
@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')  # veya başka bir sayfaya yönlendirme yapabilirsiniz
    return render(request, 'users/delete_profile.html')
"""


"""
@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/account.html', context)
"""


"""
@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)
"""
