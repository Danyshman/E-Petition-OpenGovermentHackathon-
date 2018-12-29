from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from django.contrib import messages
from listings.models import Listing


def comment(request):
    if request.method == 'POST':
        comment_body = request.POST['comment']
        listing_id = request.POST['listing_id']
        listing = get_object_or_404(Listing, pk=listing_id)
        if request.user.is_authenticated:
            comment = Comment(
                user=request.user,
                listing=listing,
                body=comment_body,
            )
            comment.save()
            messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
            return redirect('/listings/' + listing_id)
