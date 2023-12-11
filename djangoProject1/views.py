from django.shortcuts import render

from reviews.models import Business


def index(request):
    business = Business.objects.filter()
    return render(request, "main.html", {"business": business})

def search_bar(request):
    return render(request, "cafes_template.html")
