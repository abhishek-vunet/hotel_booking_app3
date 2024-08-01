# serializers.py
from rest_framework import serializers
from .models import Booking, PendingBooking, Check_in,Check_out

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class PendingBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingBooking
        fields = "__all__"

    def validate(self, data):
        room = data.get('room')
        booked_from = data.get('booked_from')
        booked_till = data.get('booked_till')

        # Retrieve all current bookings for the specified room
        current_bookings = Booking.objects.filter(room=room)

        if not current_bookings:
            return data

        errors = {}
        overlapping_bookings = []

        for booking in current_bookings:
            existing_booked_from = booking.booked_from
            existing_booked_till = booking.booked_till
            
            # Check for overlap
            if (booked_from < existing_booked_till) and (booked_till > existing_booked_from):
                overlapping_bookings.append({
                    "id": booking.id,
                    "booked_from": existing_booked_from,
                    "booked_till": existing_booked_till
                })
        
        if overlapping_bookings:
            errors['room'] = {
                "message": "Room is already booked during the requested period.",
                "overlapping_bookings": overlapping_bookings
            }
            raise serializers.ValidationError(errors)

        return data
           
class Check_inSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_in
        fields = "__all__"

class Check_outSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_out
        fields = "__all__"
    
    def validate(self, data):
        # find check_in for that booking from Check_in
        cur_check_out = data.get('check_out')
        cur_booking = data.get('booking')
        try:
            cur_check_in = Check_in.objects.get(booking=cur_booking.id).check_in
            print(cur_check_in)
        except Check_in.DoesNotExist:
            raise serializers.ValidationError({"check_out":"Please Do check_in first"})

        if cur_check_in >= cur_check_out:
            raise serializers.ValidationError({"check_out":"Check_out_time should later than check_in time"})
        return data