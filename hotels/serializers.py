# serializers.py
from rest_framework import serializers
from .models import Hotel,Review,Room,Amenities
from .validators import validate_phone_number, validate_email

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_phone', 'hotel_email', 'hotel_description']

    def validate_hotel_phone(self, value):
        validate_phone_number(value)
        return value

    def validate_hotel_email(self, value):
        validate_email(value)
        return value

    def validate(self, data):
        errors = {}
        if not data.get('hotel_name'):
            errors['hotel_name'] = "Hotel name is required."
        if errors:
            raise serializers.ValidationError(errors)
        return data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','hotel','customer','reviews','created_at']

    # def validate_hotel(self, value):
    #     if_present_hotel_id(value)
    #     return value