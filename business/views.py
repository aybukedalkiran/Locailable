from django.shortcuts import render
from restaurants.models import Customer, Business

def cafes_view(request):
    # books = ["Skin in the Game", "Antifragle", "Da Vinci's Code", "Blink", "Tesla"]

    return render(request, "rest_template.html")