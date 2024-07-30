from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField()