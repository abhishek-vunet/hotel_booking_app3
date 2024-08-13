from django import forms
from customer.models import Customer
from hotels.models import Room
from .models import Booking

class PendingBookingForm(forms.Form):
    room = forms.ModelChoiceField(label="Room", queryset=Room.objects.all(), empty_label="Select a Room")
    customer = forms.ModelChoiceField(label="Customer", queryset=Customer.objects.all(), empty_label="Select a Customer")
    booked_from = forms.DateTimeField(label="Booked From")
    booked_till = forms.DateTimeField(label="Booked Till")
    payment = forms.BooleanField(label="Payment Status")

class BookingForm(forms.Form):
    room = forms.ModelChoiceField(label="Room", queryset=Room.objects.all(), empty_label="Select a Room")
    customer = forms.ModelChoiceField(label="Customer", queryset=Customer.objects.all(), empty_label="Select a Customer")
    booked_from = forms.DateTimeField(label="Booked From")
    booked_till = forms.DateTimeField(label="Booked Till")

class CheckInForm(forms.Form):
    booking = forms.ModelChoiceField(label="Booking", queryset=Booking.objects.all(), empty_label="Select a Booking")
    check_in = forms.DateTimeField(label="Check-in Time")

class CheckOutForm(forms.Form):
    booking = forms.ModelChoiceField(label="Booking", queryset=Booking.objects.all(), empty_label="Select a Booking")
    check_out = forms.DateTimeField(label="Check-out Time")
