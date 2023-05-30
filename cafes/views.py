from django.shortcuts import render
from cafes.models import Business

def cafes_view(request):
    business = Business.objects.filter()
    return render(request, "cafes_template.html", {"business":business})


def get_loc_from(request):
    return render(request, "cafes_template.html")

