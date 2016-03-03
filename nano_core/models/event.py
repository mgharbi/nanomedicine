from django.db import models
from django.utils.translation import ugettext_lazy as _

class Event(models.Model):
    title       = models.CharField(max_length = 50)
    start       = models.DateTimeField(blank  = True)
    end         = models.DateTimeField(blank  = True)
    description = models.TextField()
    place       = models.CharField(max_length = 100, blank=True)
    url         = models.CharField(max_length = 200, blank=True)

    image   = models.FileField(upload_to = 'news_image', blank = True)

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
