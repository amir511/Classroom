from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class StudentsProfilesIndexPage(Page):
    class_name = models.CharField(max_length=255)
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('class_name', classname="full"),
        FieldPanel('description', classname="full"),
    ]


class StudentProfilePage(Page):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    mobile_number = models.CharField(max_length=255)
    email = models.EmailField()
    comments = RichTextField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', null=True, default=None, on_delete=models.CASCADE, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('birthday'),
        FieldPanel('mobile_number'),
        FieldPanel('email'),
        FieldPanel('comments'),
        ImageChooserPanel('image'),
    ]


