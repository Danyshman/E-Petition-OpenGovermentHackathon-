from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from constants import status_filter_choice, users_form_filter_choice, created_date_filter_choice, form_category
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


def users_listings(request):
    if request.user.is_authenticated:
        listings = Listing.objects.filter(user=request.user)
        paginator = Paginator(listings, 6)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        context = {
            'listings': paged_listings
        }
        return render(request, 'listings/listings.html', context)
    else:
        messages.error(request, 'Чтобы посмотреть свои заявку, вы должны быть залогинены')
        return redirect('login')


def listing(request, listing_id):
    if request.method == 'POST':
        print('hello')
    listing = get_object_or_404(Listing, pk=listing_id)
    comments = Comment.objects.filter(listing=listing)
    context = {
        'listing': listing,
        'comments': comments
    }
    return render(request, 'listings/listing.html', context)


def rate(request, listing_id, rate):
    if request.user.is_authenticated:
        listing = get_object_or_404(Listing, pk=listing_id)
        if request.user in listing.rated_forms_id.all():
            messages.error(request, 'Вы уже оценили данную заявку')
            return redirect('listing', listing_id)
        else:
            listing.total_rate += rate
            listing.num_of_rates += 1
            listing.average_rate = listing.total_rate / listing.num_of_rates
            listing.rated_forms_id.add(request.user)
            listing.save()
            messages.success(request, 'Вы успешно оценили данную заявку')
            return redirect('listing', listing_id)
    else:
        messages.error(request, 'Чтобы оценить заявку, вы должны быть залогинены')
        return redirect('login')


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            category = request.POST['category']
            address = request.POST['address']
            description = request.POST['description']
            user = request.user
            form = Listing(
                title=title,
                category=category,
                address=address,
                photo_description_1=request.FILES['photo_description_1'],
                photo_description_2=request.FILES['photo_description_2'],
                description=description,
                user=user
            )
            form.save()
            return redirect('index')
    else:
        messages.error(request, 'Чтобы создать заявку, вы должны быть залогинены')
        return redirect('login')
    return render(request, 'listings/create_form.html')


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
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'status_filter_choice': status_filter_choice,
        'users_form_filter_choice': users_form_filter_choice,
        'created_date_filter_choice': created_date_filter_choice,
        'listings': paged_listings,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
