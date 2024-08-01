# serializers.py
from rest_framework import serializers
from .models import Hotel,Review,Room,Amenities
from .validators import validate_phone_number, validate_email

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"

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
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

    def validate(self,data):
        #all the rooms which this room_numberfiltered_hotels
        current_room = data.get('room_number')
        filtered_rooms = Room.objects.filter(room_number=current_room)
        current_hotel = data.get('hotel')

        hotels = []
        for room in filtered_rooms:
            temp_hotel = room.hotel.id
            hotels.append(temp_hotel)
            if current_hotel.id in hotels:
                raise serializers.ValidationError({"room_number":"This room number is already present in this hotel"})

        return data

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Amenities
        fields = "__all__"
    