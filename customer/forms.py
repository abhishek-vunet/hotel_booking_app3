from django import forms
from .models import Customer

class CustomerForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    customer_phone = forms.IntegerField(label="Customer Phone")
    customer_email = forms.EmailField(label= "Customer Email")
