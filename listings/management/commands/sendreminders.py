from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from datetime import date, timedelta

from e_petition.settings import APP_URL
from constants import government_branch_emails
from listings.models import Listing


class Command(BaseCommand):
    help = 'checks whether there are listing items that haven\'t been processed in two weeks ' \
           'and sends emails to corresponding government branches'

    def handle(self, *args, **kwargs):
        time_threshold = date.today() - timedelta(days=14)
        unnoticed_listings = Listing.objects.filter(status='pending', created_date__lt=time_threshold)

        mail_subject = 'Unprocessed petition.'

        for listing in unnoticed_listings:
            message = render_to_string('listings/reminder_email.html', {
                'APP_URL': APP_URL,
                'listing': listing,
            })
            to_email = [government_branch_emails[listing.category]]
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
