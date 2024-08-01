from django.db import models
from django.utils import timezone
from customer.models import Customer

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=30, blank=False, null=False)
    hotel_phone = models.BigIntegerField(blank=False, null=False,unique=True)
    hotel_email = models.EmailField(blank=False, null=False)
    hotel_description = models.TextField(max_length=200,blank=True, null=False)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.SET_NULL,related_name='reviews') #hotel_id
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL,related_name='reviews') #customer_id
    reviews = models.TextField(max_length=200,blank=False,null=False)
    created_at = models.DateTimeField(default=timezone.now)

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10, blank=False, null=False)
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.SET_NULL,related_name='rooms') #hotel_id
    room_description = models.TextField(max_length=200,blank=True, null=False)
    price = models.IntegerField(null=True,blank=True)

class Amenities(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room,null=True, on_delete=models.SET_NULL,related_name='amenities',unique=True) #room_id
    ac =  models.BooleanField(blank=False,null=False)
    number_of_beds = models.IntegerField(blank=False,null=False)
    balcony = models.BooleanField(blank=False, null=False)
    flour_num = models.IntegerField(blank=False, null=False)





