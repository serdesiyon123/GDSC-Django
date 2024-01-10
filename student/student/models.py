from django.db import models
from advisor.models import Advisor

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE,related_name='const')
