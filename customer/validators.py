# validators.py
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    """Validate phone number."""
    if len(str(value)) != 10:
        raise ValidationError("Phone number must be exactly 10 digits long.")

def validate_email(value):
    """Ensure the email address is valid."""
    if '@' not in value:
        raise ValidationError("Enter a valid email address.")
