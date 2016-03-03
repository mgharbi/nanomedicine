from django.contrib.auth.models import User
from django.db import models

class Publication(models.Model):
    title   = models.CharField(max_length       = 1000)
    authors = models.CharField(max_length       = 1000)
    content = models.TextField()
    date    = models.IntegerField()
    pdf     = models.FileField(upload_to = 'publication_pdf', blank = True)

    owners  = models.ManyToManyField(User)

    class Meta:
        unique_together = ('title', 'date', 'authors')

    # TODO: Parse bibtex pre-save
