from django.shortcuts import render
from .models import Business
from .forms import BusinessSearchForm
def business_detail(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    return render(request, 'businesses/business_detail.html', {'business': business})

def home(request):
    business = Business.objects.all()

    context = {
        'cafes': business,
    }

    return render(request, 'business/home.html', context)

def business_search(request):
    businesses = Business.objects.all()
    form = BusinessSearchForm(request.GET)
    error_message = ''

    if form.is_valid():
        business_name_query = form.cleaned_data.get('business_name')
        address_query = form.cleaned_data.get('address')

        if business_name_query:
            businesses = businesses.filter(business_name__icontains=business_name_query)
        if address_query:
            businesses = businesses.filter(address__icontains=address_query)

        if not businesses.exists():
            error_message = 'Business not found.'

    context = {'businesses': businesses, 'form': form, 'error_message': error_message}
    return render(request, 'business_search.html', context)

"""def cafes_view(request):
    business = Business.objects.filter(emai)
    return render(request, "rest_template.html")


def get_login_form(request, businessCafe):
    return render(request, "login_form.html")


def cafe_arttir(request, businessCafe):
    business = Business.objects.filter()
    business += 1
    business.save()

    return render(request, "rest_template.html")


def cafe_azalt(request):
    business = Business.objects.filter()
    business -= 1
    business.save()

    return render(request, "rest_template.html")


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['lastname']

    business = Business.objects.filter(email=email)

    return render(request, "business_cafe.html", {'cafe' :Business.cafe})
"""