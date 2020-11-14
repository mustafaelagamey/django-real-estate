from django.shortcuts import render
from .models import Listing


# Create your views here.
def listings_index(request):
    context = {
        'listings': Listing.objects.all()
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')
