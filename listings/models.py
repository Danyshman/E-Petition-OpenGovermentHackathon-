from django.db import models
from django.contrib.auth.models import User
from constants import form_status, form_category
from django.utils import timezone


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(choices=form_category, max_length=100)
    average_rate = models.DecimalField(default=0, blank=True, decimal_places=1, max_digits=10)
    num_of_rates = models.DecimalField(decimal_places=0, max_digits=10, default=0, blank=True)
    total_rate = models.DecimalField(decimal_places=1, max_digits=10, default=0, blank=True)
    status = models.CharField(choices=form_status, max_length=200, blank=True, default=form_status[0][0])
    photo_description_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_description_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_result_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_result_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    closed_date = models.DateTimeField(default=timezone.now, blank=True)
    rated_forms_id = models.ManyToManyField(User, blank=True, related_name='rated_forms_id')
    num_of_comments = models.DecimalField(decimal_places=0, max_digits=10, default=0, blank=True)

    def __str__(self):
        return self.title
