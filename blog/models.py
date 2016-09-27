from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    
    # text defined with limited number of characters
    title = models.CharField(max_length=200)

    # long text without limt (i.e BLOG post)
    text = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)

    # link to another model
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
