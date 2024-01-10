from django.db import models

class Advisor(models.Model):
    name = models.TextField()
    email = models.EmailField()