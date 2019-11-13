from django.db import models
from wagtail.core.models import Page


# Create your models here.
class BlogListPage(Page):
    pass


class BlogPostPage(Page):

    template = "blog/post.html"

