from django.shortcuts import render

from cafes.models import Business


def index(request):
    business = Business.objects.filter()
    return render(request, "main.html", {"business": business})

def search_bar(request):
    return render(request, "cafe_template.html")
