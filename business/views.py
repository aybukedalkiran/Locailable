from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Business, Availability, Review
from .forms import BusinessForm, AvailabilityForm, ReviewForm
from .utils import searchBusiness
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def is_business_owner(request, user_business):
    return user_business.user == request.user


def business_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            business = Business.objects.create(user=user)

            if user and business:
                login(request, user)
                return redirect('business_detail', business_id=business.id)
            else:
                return HttpResponse("Kullanıcı veya işletme oluşturulamadı.")
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'business/business_signup.html', context)  #signup.html yapıcam


@login_required
def business_login(request):
    try:
        user_business = Business.objects.get(user=request.user)
    except Business.DoesNotExist:
        user_business = None

    if user_business and is_business_owner(request, user_business):
        return redirect('business_detail', business_id=user_business.id)
    else:
        return render(request, 'business/business_login.html', {'user_business': user_business})


@login_required
def business_logout(request):
    logout(request)
    return redirect('business')  # veya başka bir sayfaya yönlendirme yapabilirsiniz


@login_required
def update_business(request):
    try:
        user_business = Business.objects.get(user=request.user)
    except Business.DoesNotExist:
        user_business = None

    if user_business and is_business_owner(request, user_business):
        if request.method == 'POST':
            form = BusinessForm(request.POST, instance=user_business)
            if form.is_valid():
                form.save()
                return redirect('business_detail', business_id=user_business.id)
        else:
            form = BusinessForm(instance=user_business)

        return render(request, 'business/update_business.html', {'form': form})
    else:
        return HttpResponse("Bu işletme size ait değil.")


def business_detail(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    availability = business.availability
    reviews = business.review_set.all()
    return render(request, 'business/business_detail.html', {'business': business, 'availability': availability, 'reviews': reviews})


def business(request):
    business, search_query = searchBusiness(request)

    context = {'business': business,
               'search_query': search_query}
    return render(request, 'business/business.html', context)


def create_availability(request, business_id):
    business = get_object_or_404(Business, id=business_id)

    if business.availability:
        availability = business.availability
    else:
        availability = Availability(business=business)

    if request.method == 'POST':
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            return redirect('business_detail', business_id=business.id)
    else:
        form = AvailabilityForm(instance=availability)

    return render(request, 'business/create_availability.html', {'form': form, 'business': business})


def create_review(request, business_id):
    business = get_object_or_404(Business, id=business_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.business = business
            review.save()
            return redirect('business_detail', business_id=business.id)
    else:
        form = ReviewForm()

    return render(request, 'business/create_review.html', {'form': form, 'business': business})



"""
def home(request):
    business = Business.objects.all()
    context = {'cafes': business}
    return render(request, 'business/home.html', context)
"""


"""
@login_required
def business_login(request):
    try:
        user_business = Business.objects.get(user=request.user)
    except Business.DoesNotExist:
        user_business = None

    return render(request, 'business_login.html', {'user_business': user_business})
"""


"""
@login_required
def update_business(request):
    user_business = Business.objects.get(user=request.user)

    # işletme sahibi olup olmadığını kontrol et
    if user_business.user != request.user:
        return HttpResponse("Bu işletme size ait değil.")

    if request.method == 'POST':
        form = BusinessUpdateForm(request.POST, instance=user_business)
        if form.is_valid():
            form.save()
            return redirect('business_login')
    else:
        form = BusinessUpdateForm(instance=user_business)

    return render(request, 'update_business.html', {'form': form})
"""




"""
def business_detail(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    reviews = Review.objects.filter(business=business)
    return render(request, 'business/business_detail.html', {'business': business, 'reviews': reviews})
"""


"""
@login_required(login_url="login")
def create_business(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = profile
            business.save()

            return redirect()
    else:
        form = BusinessForm()

    context = {'form': form}
    return render(request, 'business/create_business.html', context)
"""


"""
@login_required(login_url="login")
def update_business(request, business_id):
    #profile = request.user.profile
    business = get_object_or_404(Business, id=business_id, owner__user=request.user)
    form = BusinessForm(instance=business)

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES, instance=business)
        if form.is_valid():
            business = form.save()

            return redirect('business_detail', business_id=business.id)

    context = {'form': form, 'business': business}
    return render(request, "business/update_business.html", context)
"""
"""
@login_required(login_url="login")
def delete_business(request, business_id):
    business = get_object_or_404(Business, id=business_id, owner__user=request.user)
    
    if request.method == 'POST':
        business.delete()
        return redirect('business_detail')  # Use the appropriate named URL for listing businesses
    
    context = {'object': business}
    return render(request, 'business/delete_template.html', context)
"""



#def create_business_owner(request):
#    if request.method == 'POST':
#        form = BusinessOwnerForm(request.POST)
#        if form.is_valid():
#            business_owner = form.save()
#            return redirect('business_detail', business_id=business_owner.business.id)
#    else:
#        form = BusinessOwnerForm()
#
#    return render(request, 'create_business_owner.html', {'form': form})
