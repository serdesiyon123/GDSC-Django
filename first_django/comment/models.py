from django.db import models

class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField()
