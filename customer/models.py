from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    customer_phone = models.BigIntegerField(blank=False, null=False,unique=True)
    customer_email = models.EmailField(blank=False, null=False)

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
