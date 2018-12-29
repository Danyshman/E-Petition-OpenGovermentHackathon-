from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
from constants import status_filter_choice, users_form_filter_choice
from comments.models import Comment


def index(request):
    listings = Listing.objects.order_by('created_date')
    paginator = Paginator(listings,  6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    comments = Comment.objects.filter(listing=listing)
    context = {
        'listing': listing,
        'comments': comments
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('created_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title=title)
    if 'address' in request.GET:
        address = request.GET['address']
        if address:
            queryset_list = queryset_list.filter(address=address)
    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            queryset_list = queryset_list.filter(status=status)
    if 'created_date' in request.GET:
        created_date = request.GET['created_date']
        if created_date:
            queryset_list = queryset_list.order_by('-created_date')
    context = {
        'form_filter_choices': status_filter_choice,
        'specific_filter_choice': users_form_filter_choice,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
