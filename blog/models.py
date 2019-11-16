from django.db import models
from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.routable_page.models import route, RoutablePageMixin

from modelcluster.fields import ParentalManyToManyField

from streams import blocks


@register_snippet
class BlogCategory(models.Model):
    """Blog Category for a snippet"""

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        max_length=255,
        help_text="A slug to identify posts by this category",
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    class Meta: # noqa
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class BlogListPage(RoutablePageMixin, Page):

    template = "blog/list.html"
    max_count = 1
    subpage_types = ['blog.BlogPostPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts = BlogPostPage.objects.live().public().order_by("-first_published_at")

        # if request.GET.get('tag', None):
        #     tags = request.GET.get('tag')
        #     all_posts = all_posts.filter(tags__slug__in=[tags])

        paginator = Paginator(all_posts, 10)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        context['categories'] = BlogCategory.objects.all()
        return context

    @route(r"category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog post based on a category"""
        context = self.get_context(request)

        try:
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            category = None

        if category is None:
            pass

        context["posts"] = BlogPostPage.objects.live().public().filter(categories__in=[category]).order_by("-first_published_at")
        context["cat_slug"] = cat_slug
        return render(request, "blog/list.html", context)


class BlogPostPage(Page):

    template = "blog/post.html"
    subpage_types = []
    parent_page_types = ['blog.BlogListPage', 'home.HomePage']

    intro = models.CharField(max_length=255, blank=False, null=True)

    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)

    content = StreamField(
        [
            ('inline_image', blocks.InlineImageBlock()),
            ('paragraph', blocks.SimpleRichTextBlock()),
            ('subscribe', blocks.SubscribeBlock()),
        ],
        null=True,
        blank=False,
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel("cover_image"),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
            ],
            heading="Categories",
        ),
        StreamFieldPanel("content")
    ]
