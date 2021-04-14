from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:75]

    def format_time(self):
        return self.pubdate.strftime('%b %d, %Y')
