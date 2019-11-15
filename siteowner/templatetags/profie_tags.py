from django import template

from ..models import AuthorProfile


register = template.Library()


@register.inclusion_tag
def get_profile():
    return AuthorProfile.objects.get(pk=1)
