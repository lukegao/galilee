from django import template

from ..models import AuthorProfile


register = template.Library()


@register.simple_tag
def get_profile():
    try:
        neo = AuthorProfile.objects.get()
    except Exception:
        neo = None
    return neo
