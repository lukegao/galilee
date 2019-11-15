from django.db import models

from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPostPage


@register_snippet
class AuthorProfile(models.Model):
    """Profile for author."""

    first_name = models.CharField(max_length=50, blank=False, null=False, default="Luke")
    family_name = models.CharField(max_length=50, blank=False, null=False, default="Gao")
    avatar = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        blank=False,
        null=True
    )

    intro = models.CharField(max_length=255, blank=False, null=True)
    github = models.URLField(verbose_name="github account", name='github')
    wechat = models.URLField(verbose_name="wechat id", name='wechat')
    linkedin = models.URLField(verbose_name="linkedin account", name='linkedin')
    twitter = models.URLField(verbose_name="twitter account", name='twitter')

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('first_name'),
                FieldPanel('family_name'),
                ImageChooserPanel('avatar'),
            ],
            heading='Name and avatar'
        ),
        FieldPanel('intro'),
        MultiFieldPanel(
            [
                FieldPanel('github'),
                FieldPanel('linkedin'),
                FieldPanel('wechat'),
                FieldPanel('twitter'),
            ],
            heading='Social media',
        )
    ]


class HomePage(Page):

    template = "home.html"
    max_count = 1

    def get_context(self, request, *args, **kwags):
        context = super().get_context(request, *args, **kwags)

        latest_posts = BlogPostPage.objects.live().public().order_by('-first_published_at')[:10]

        context["posts"] = latest_posts
        return context
