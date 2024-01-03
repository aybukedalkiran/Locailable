from .models import Business
from django.shortcuts import redirect
from django.db.models import Q

def searchBusiness(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    address = Business.objects.filter(address__icontains=search_query)

    business = Business.objects.distinct().filter(
        Q(business_name__icontains=search_query) |
        Q(address__in=address)
    )
    # Return a redirect response to the search_results view
    return redirect('search_results', search_query=search_query)



"""def searchBusiness(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    address = Business.objects.filter(address__icontains=search_query)

    business = Business.objects.distinct().filter(
        Q(business_name__icontains=search_query) |
        Q(address__in=address)
    )
    return redirect('search_results', search_query=search_query)"""
