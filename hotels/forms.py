from django import forms
from customer.models import Customer
from .models import Hotel,Room

class HotelForm(forms.Form):
    hotel_name = forms.CharField(label="Hotel Name", max_length=30)
    hotel_phone = forms.IntegerField(label="Hotel Phone")
    hotel_email = forms.EmailField(label= "Hotel Email")
    hotel_description = forms.CharField(label="Hotel Description", max_length=200)

class ReviewForm(forms.Form):
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), label="Hotel", empty_label="Select a Hotel")
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label="Customer", empty_label="Select a Customer")
    reviews = forms.CharField(label="Review", max_length=200, widget=forms.Textarea)

class RoomForm(forms.Form):
    room_number = forms.CharField(label="Room Number", max_length=10)
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), label="Hotel", empty_label="Select a Hotel")
    room_description = forms.CharField(label="Room Description", max_length=200, widget=forms.Textarea, required=False)
    price = forms.IntegerField(label="Price", required=False)

class AmenityForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Room.objects.all(), label="Room", empty_label="Select a Room", required=True)
    ac = forms.BooleanField(label="Air Conditioning", required=False)
    number_of_beds = forms.IntegerField(label="Number of Beds", required=True)
    balcony = forms.BooleanField(label="Balcony", required=False)
    flour_num = forms.IntegerField(label="Floor Number", required=True)
