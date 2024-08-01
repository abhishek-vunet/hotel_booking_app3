from django.db import models
from django.utils import timezone
from customer.models import Customer
from hotels.models import Room

class PendingBooking(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL,related_name='pendingBookings') #room_id
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL,related_name='pendingBookings') #customer_id
    booked_from = models.DateTimeField(blank=False,null=False)
    booked_till = models.DateTimeField(blank=False,null=False)
    payment = models.BooleanField(blank=False,null=False)

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL,related_name='bookings') #room_id
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL,related_name='bookings') #customer_id
    booked_from = models.DateTimeField(blank=False,null=False)
    booked_till = models.DateTimeField(blank=False,null=False)

class Check_in(models.Model):
    id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.SET_NULL,related_name='check_in',unique=True)
    check_in = models.DateTimeField(blank=False,null=False)

class Check_out(models.Model):
    id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.SET_NULL,related_name='check_out',unique=True)
    check_out = models.DateTimeField(blank=False,null=False)







