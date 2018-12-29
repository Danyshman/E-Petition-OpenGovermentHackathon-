from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'address', 'created_date')
    list_display_links = ('id', 'user', 'title', 'address', 'created_date',)
    search_fields = ('id', 'title', 'address', 'status')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
