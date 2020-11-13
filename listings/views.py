from django.shortcuts import render


# Create your views here.
def listings_index(request):
    return render(request, 'listings/listings.html')


def listing(request,listing_id):
    return render(request, 'listings/listing.html')
