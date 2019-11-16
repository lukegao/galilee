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


class SimpleRichTextBlock(blocks.RichTextBlock):
    """RichText without media features."""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(required=required, help_text=help_text, editor=editor, features=features, validators=validators, **kwargs)
        self.features = [
            "bold", "italic", "link",
            "ol", "ul", "hr", "h2",
            "h3", "h4", "document-link",
            "code", "blockquote", "subscript"
            ]

    class Meta: # noqa
        template = "streams/post.html"
        icon = 'edit'
        label = 'Post Body'
