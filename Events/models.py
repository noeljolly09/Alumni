from django.db import models
from django.urls import reverse

# Create your models here.
class eventsData(models.Model):
    event_name = models.CharField(max_length=20)
    event_image = models.ImageField(blank=True, null=True, upload_to="event_images/",default="default.jpg")
    event_date = models.DateField()
    event_time = models.TimeField(default="15:00")
    event_description = models.CharField(max_length=300)
    creation_date = models.DateField()

    def __str__ (self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('allevents')

