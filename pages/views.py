from django.shortcuts import render
from listings.models import Listing
from constants import status_filter_choice, users_form_filter_choice, created_date_filter_choice


def index(request):
    listings = Listing.objects.all().exclude(status='completed')[:3]
    context = {
        'status_filter_choice': status_filter_choice,
        'users_form_filter_choice': users_form_filter_choice,
        'created_date_filter_choice': created_date_filter_choice,
        'listings': listings
    }
    return render(request, 'pages/index.html', context)
