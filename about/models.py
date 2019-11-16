from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.models import ParentalKey


class AboutPage(Page):
    """About Page Model"""

    template = "about/about.html"
    parental_page_types = ['home.HomPage']
    subpage_types = []

    body = RichTextField(blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('projects', label='Side Projects'),
    ]


class ProjectItem(Orderable):
    """Project Item to show in the carousel"""

    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=255, blank=False, null=True)
    project_url = models.URLField(blank=True, null=True)

    snapshot = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        blank=False,
        null=True,
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('project_url'),
        ImageChooserPanel('snapshot'),
    ]

    class Meta: # noqa
        verbose_name = "Side Project"
        verbose_name_plural = "Side Projects"

    def __str__(self):
        return self.name
