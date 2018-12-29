from django.db import models
from listings.models import Listing
from datetime import datetime
from django.contrib.auth.models import User


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
