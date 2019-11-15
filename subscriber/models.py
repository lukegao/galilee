from django.db import models
from wagtail.api import APIField


class Subscriber(models.Model):
    """Subscriber to site mails"""

    email_addr = models.EmailField(blank=False, unique=True)
    date = models.DateTimeField(null=False)

    api_fields = [
        APIField('email_addr')
    ]

    def __str__(self):
        return self.email_addr

    class Meta: # noqa
        verbose_name = 'Mail Subsrciber'
        verbose_name_plural = 'Mail Subscribers'
