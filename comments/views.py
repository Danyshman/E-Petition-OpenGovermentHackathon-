from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from django.contrib import messages
from listings.models import Listing


def comment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_body = request.POST['comment']
            listing_id = request.POST['listing_id']
            listing = get_object_or_404(Listing, pk=listing_id)
            comment = Comment(
                user=request.user,
                listing=listing,
                body=comment_body,
            )
            listing.num_of_comments += 1
            listing.save()
            comment.save()
            messages.success(request, 'Вы успешно прокоментировали данную заявку')
            return redirect('/listings/' + listing_id)
    else:
        messages.error(request, 'Чтобы прокоментировать заявку, вы должны быть залогинены')
        return redirect('login')
