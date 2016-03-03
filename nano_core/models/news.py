from django.db import models

class News(models.Model):
    title   = models.CharField(max_length       = 50)
    content = models.TextField()
    date    = models.DateTimeField(auto_now_add = True)
    image   = models.FileField(upload_to = 'news_image', blank = True)

    class Meta:
        verbose_name_plural = "news"
