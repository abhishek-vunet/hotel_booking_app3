# serializers.py
from rest_framework import serializers
from .models import Customer
from .validators import validate_phone_number, validate_email

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'customer_phone', 'customer_email']

    def validate_customer_phone(self, value):
        print(value)
        validate_phone_number(value)
        return value

    def validate_customer_email(self, value):
        validate_email(value)
        return value

    def validate(self, data):
        errors = {}
        if not data.get('first_name'):
            errors['first_name'] = "First name is required."
        if not data.get('last_name'):
            errors['last_name'] = "Last name is required."
        if errors:
            raise serializers.ValidationError(errors)
        return data
