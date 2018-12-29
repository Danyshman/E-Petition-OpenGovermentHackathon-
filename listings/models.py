from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from constants import form_status


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField()
    average_rate = models.FloatField(default=0, blank=True)
    num_of_rates = models.DecimalField(decimal_places=1, max_digits=10, default=0, blank=True)
    total_rate = models.DecimalField(decimal_places=1, max_digits=10, default=0, blank=True)
    status = models.CharField(choices=form_status, max_length=200, blank=True, default=form_status[0])
    photo_description_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_description_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_result_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_result_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    closed_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
