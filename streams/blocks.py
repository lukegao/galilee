"""Implementaion of StreamFields."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class InlineImageBlock(blocks.StructBlock):
    """Image in paragraph."""

    description = blocks.CharBlock(
        required=True,
        help_text="Add image description."
    )

    image = ImageChooserBlock(required=True)

    class Meta: # noqa
        template = 'streams/inline_image.html'
        icon = "image"
        label = "Inlined Image"


class SubscribeBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Subscribe Title")
    intro = blocks.TextBlock(required=True)
    email = blocks.EmailBlock(required=True)

    class Meta: # noqa
        template = "streams/subscribe.html"
        icon = 'placeholder'
        label = 'Subscribe'


class SimpleRichTextBlock(blocks.RichTextBlock):
    """RichText without media features."""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(required=required, help_text=help_text, editor=editor, features=features, validators=validators, **kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta: # noqa
        template = "streams/post.html"
        icon = 'edit'
        label = 'Post Body'
