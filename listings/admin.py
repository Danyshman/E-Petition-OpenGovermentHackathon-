from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'address', 'status')
    list_display_links = ('id', 'user', 'title', 'address', 'status',)
    search_fields = ('id', 'title', 'address', 'status')
    list_per_page = 10


admin.site.register(Listing, ListingAdmin)
