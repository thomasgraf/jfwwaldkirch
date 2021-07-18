from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        InlinePanel('hero_images', label='Hero Images'),
        FieldPanel('body', classname="full"),

    ]


class HeroGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='hero_images')
    hero_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    hero_slogan = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('hero_image'),
        FieldPanel('hero_slogan'),
    ]


# Keep the definition of BlogIndexPage, and add:


class WebPage(Page):


    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        InlinePanel('slider_images', label="Slider images"),
        FieldPanel('body', classname="full"),

    ]

class WebPageGalleryImage(Orderable):
    page = ParentalKey(WebPage, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
