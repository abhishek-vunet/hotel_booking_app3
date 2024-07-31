# validators.py
from django.core.exceptions import ValidationError
from .models import Hotel
def validate_phone_number(value):
    """Validate phone number."""
    print(value)
    if len(str(value)) != 10:
        raise ValidationError("Phone number must be exactly 10 digits long.")

def validate_email(value):
    """Ensure the email address is valid."""
    if '@' not in value:
        raise ValidationError("Enter a valid email address.")

# def if_present_hotel_id(value):
#     print(value)
#     if value != 2:
#         raise ValidationError("This hotel is not valid.")