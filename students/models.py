from django.db import models

from modelcluster.fields import ParentalManyToManyField

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ClassPage(Page):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = self.slug if self.slug else 'slug_will_be_generated_automatically'
    
    class_name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    
    content_panels = [
        FieldPanel('class_name', classname="full"),
        FieldPanel('description', classname="full"),
    ]
    
    def save(self, *args, **kwargs):
        self.title = self.class_name
        self.slug = "-".join(self.class_name.lower().split())
        super().save(*args, **kwargs)

class StudentPage(Page):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = self.slug if self.slug else 'slug_will_be_generated_automatically'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    mobile_number = models.CharField(max_length=255)
    email = models.EmailField()
    comments = RichTextField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, default=None, related_name='+')

    content_panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('birthday'),
        FieldPanel('mobile_number'),
        FieldPanel('email'),
        FieldPanel('comments'),
        ImageChooserPanel('image'),
    ]

    def save(self, *args, **kwargs):
        self.title = self.first_name + " " + self.last_name
        self.slug = "-".join(self.title.lower().split())
        super().save(*args, **kwargs)

class AttendancePage(Page):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = self.slug if self.slug else 'slug_will_be_generated_automatically'

    date = models.DateField()
    students = ParentalManyToManyField(StudentPage, related_name='attendances')

    content_panels = [
        FieldPanel('date'),
        FieldPanel('students'),
    ]

    def save(self, *args, **kwargs):
        self.title = 'Att:' + str(self.date)
        self.slug = str(self.date)
        super().save(*args, **kwargs)
