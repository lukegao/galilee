from wagtail.core.models import Page
from blog.models import BlogPostPage


class HomePage(Page):

    template = "home.html"
    max_count = 1

    def get_context(self, request, *args, **kwags):
        context = super().get_context(request, *args, **kwags)

        latest_posts = BlogPostPage.objects.live().public().order_by('-first_published_at')[:10]

        context["posts"] = latest_posts
        return context
