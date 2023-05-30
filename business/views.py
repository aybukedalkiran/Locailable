from django.shortcuts import render
from cafes.models import Business



def cafes_view(request):
    business = Business.objects.filter(cafe)
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

    business = Business.objects.filter(email_exact=email)

    return render(request, "business_cafe.html", {'cafe' :Business.cafe})
