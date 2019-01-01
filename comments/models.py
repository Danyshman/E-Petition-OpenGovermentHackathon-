from django.db import models
from listings.models import Listing
from django.contrib.auth.models import User
from django.utils import timezone


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
