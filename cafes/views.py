from django.shortcuts import render
from cafes.models import Customer, Business

def cafes_view(request):
    # books = ["Skin in the Game", "Antifragle", "Da Vinci's Code", "Blink", "Tesla"]

    return render(request, "cafes_template.html")