from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('<int:listing_id>/rate/<int:rate>', views.rate, name='rate'),
    path('user/my-listings', views.users_listings, name='user-listings')
]