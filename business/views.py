from django.shortcuts import render
from .models import Business

def business_detail(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    return render(request, 'businesses/business_detail.html', {'business': business})


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