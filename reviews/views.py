from django.shortcuts import render
from business.models import Business
from .models import Review

def review_detail(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

##def get_loc_from(request):
    ##return render(request, "cafes_template.html")"""


