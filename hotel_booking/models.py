from django.db import models

# Create your models here.

class Customer(models.Model):

    customer_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30,default="f")
    last_name = models.CharField(max_length=30,default="f")
    customer_phone = models.BigIntegerField(default=0)
    customer_email = models.EmailField(default="null")