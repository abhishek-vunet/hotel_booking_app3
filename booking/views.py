from .models import Booking,PendingBooking,Check_in, Check_out
from .serializers import BookingSerializer,PendingBookingSerializer,Check_inSerializer,Check_outSerializer
from customer.models import Customer
from rest_framework import status # for http status
from rest_framework.response import Response 
from rest_framework.views import APIView #to define the apis
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.mail import EmailMessage

from django.shortcuts import render
from .forms import PendingBookingForm,BookingForm,CheckInForm,CheckOutForm
from rest_framework.parsers import FormParser, MultiPartParser
    
class BookingGetApiView(APIView):

    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookingGetByIdApiView(APIView):


    def get_object(self, id):
        try:
            return PendingBooking.objects.get(id=id)
        except PendingBooking.DoesNotExist:
            return None
        
    def get(self,request,id):
        booking_instance = self.get_object(id)
        if not booking_instance:
            return Response(
                {"res": "Object with booking id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookingSerializer(booking_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class BookingUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Booking.objects.get(id=id)
        except Booking.DoesNotExist:
            return None


    def put(self, request, id):
 
        booking_instance = self.get_object(id)
        if not booking_instance:
            return Response(
                {"res": "Object with booking id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data

        room = data.get("room")
        customer = data.get("customer")
        booked_from = data.get("booked_from")
        booked_till = data.get("booked_till")


        data = {
            "room" : room,
            "customer" : customer,
            "booked_from" : booked_from,
            "booked_till": booked_till,
        }

        serializer = BookingSerializer(instance = booking_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDeleteByIdApiView(APIView):

    # def get_object(self, id):

    #     try:
    #         return PendingBooking.objects.get(id=id)
    #     except PendingBooking.DoesNotExist:
    #         return None

    def delete(self, request, id):
        # booking_instance = self.get_object(id)
        Booking.objects.all().delete()
        # if not booking_instance:
        #     return Response(
        #         {"res": "Object with booking id does not exists"}, 
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        # booking_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    
class PendingBookingGetApiView(APIView):

    def get(self, request):
        pendingBookings = PendingBooking.objects.all()
        serializer = PendingBookingSerializer(pendingBookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PendingBookingGetByIdApiView(APIView):

    def get_object(self, id):
        try:
            return PendingBooking.objects.get(id=id)
        except PendingBooking.DoesNotExist:
            return None
        
    def get(self,request,id):
        pendingBooking_instance = self.get_object(id)
        if not pendingBooking_instance:
            return Response(
                {"res": "Object with PendingBooking id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PendingBookingSerializer(pendingBooking_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PendingBookingAddApiView(APIView):
    parser_classes = [FormParser, MultiPartParser]  # Add parsers to handle form data

    def get(self,request):
        return render(request, "addPendingBooking.html", {"form": PendingBookingForm})
    
    def post(self, request):
        data = request.data

        room_id = data.get("room")
        customer_id = data.get("customer")
        booked_from = data.get("booked_from")
        booked_till = data.get("booked_till")
        payment = data.get("payment")  # Assume this is a string 'True' or 'False'

        # Prepare data for serializer
        pending_booking_data = {
            "room": room_id,
            "customer": customer_id,
            "booked_from": booked_from,
            "booked_till": booked_till,
            "payment": payment
        }

        # Check if room is already booked
        serializer = PendingBookingSerializer(data=pending_booking_data)
        if serializer.is_valid():
            if payment == 'False':  # Assuming payment is a string 'True' or 'False'
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                # Handle booking creation
                booking_data = {
                    "room": room_id,
                    "customer": customer_id,
                    "booked_from": booked_from,
                    "booked_till": booked_till,
                }
                booking_serializer = BookingSerializer(data=booking_data)
                if booking_serializer.is_valid():
                    booking_serializer.save()

                    customer_mail = Customer.objects.get(id=customer_id).customer_email
                    print(customer_mail)
                    # send a mail here to the customer
                    send_mail(
                        "Hotel Booking App",
                        "Your booking has been confirmed",
                        settings.EMAIL_HOST_USER,
                        [customer_mail],
                        fail_silently=False,
                    )

                    return Response(booking_serializer.data, status=status.HTTP_201_CREATED)

                else:
                    return Response({'error': booking_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class PendingBookingUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return PendingBooking.objects.get(id=id)
        except PendingBooking.DoesNotExist:
            return None


    def put(self, request, id):
 
        pendingBooking_instance = self.get_object(id)
        if not pendingBooking_instance:
            return Response(
                {"res": "Object with pendingBooking id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data

        room = data.get("room_id")
        customer = data.get("customer_id")
        booked_from = data.get("booked_from")
        booked_till = data.get("booked_till")
        payment = data.get("payment")


        data = {
            "room" : room,
            "customer" : customer,
            "booked_from" : booked_from,
            "booked_till": booked_till,
            "payment": payment
        }

        serializer = PendingBookingSerializer(instance = pendingBooking_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PendingBookingDeleteByIdApiView(APIView):

    def get_object(self, id):

        try:
            return PendingBooking.objects.get(id=id)
        except PendingBooking.DoesNotExist:
            return None

    def delete(self, request, id):
        pendingBooking_instance = self.get_object(id)
        if not pendingBooking_instance:
            return Response(
                {"res": "Object with PendingBooking id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        pendingBooking_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    
class Check_inGetApiView(APIView):

    def get(self, request):
        Check_in_instance = Check_in.objects.all()
        serializer = Check_inSerializer(Check_in_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Check_inGetByIdApiView(APIView):

    def get_object(self, id):
        try:
            return Check_in.objects.get(id=id)
        except Check_in.DoesNotExist:
            return None
        
    def get(self,request,id):
        Check_in_instance = self.get_object(id)
        if not Check_in_instance:
            return Response(
                {"res": "Object with Check_in id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = Check_inSerializer(Check_in_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Check_inAddApiView(APIView):
    parser_classes = [FormParser, MultiPartParser]  # Add parsers to handle form data

    def get(self,request):
        return render(request, "addCheckIn.html", {"form": CheckInForm})
    
    def post(self, request):
       
        data=request.data
        booking = data.get("booking")
        check_in = data.get("check_in")

        data = {
            "booking" : booking,
            "check_in" : check_in,
        }

        # Check if room is already booked
        serializer = Check_inSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class Check_inUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Check_in.objects.get(id=id)
        except Check_in.DoesNotExist:
            return None


    def put(self, request, id):
 
        Check_in_instance = self.get_object(id)
        if not Check_in_instance:
            return Response(
                {"res": "Object with pendingBooking id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data
        booking = data.get("booking")
        check_in = data.get("check_in")


        data = {
            "booking" : booking,
            "check_in" : check_in,
        }

        serializer = Check_inSerializer(instance = Check_in_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Check_inDeleteByIdApiView(APIView):    
    
    def get_object(self, id):

        try:
            return Check_in.objects.get(id=id)
        except Check_in.DoesNotExist:
            return None

    def delete(self, request, id):
        Check_in_instance = self.get_object(id)
        if not Check_in_instance:
            return Response(
                {"res": "Object with PendingBooking id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        Check_in_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class Check_outGetApiView(APIView):

    def get(self, request):
        Check_out_instance = Check_out.objects.all()
        serializer = Check_outSerializer(Check_out_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Check_outGetByIdApiView(APIView):

    def get_object(self, id):
        try:
            return Check_out.objects.get(id=id)
        except Check_out.DoesNotExist:
            return None
        
    def get(self,request,id):
        Check_out_instance = self.get_object(id)
        if not Check_out_instance:
            return Response(
                {"res": "Object with Check_out id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = Check_outSerializer(Check_out_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

def generate_pdf(lines):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return buf

class Check_outAddApiView(APIView):

    parser_classes = [FormParser, MultiPartParser]  # Add parsers to handle form data

    def get(self,request):
        return render(request, "addCheckout.html", {"form": CheckOutForm})
    
    def post(self, request):
       
        data=request.data
        booking = data.get("booking")
        check_out = data.get("check_out")

        data = {
            "booking" : booking,
            "check_out" : check_out,
        }

        # Check if room is already booked
        serializer = Check_outSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            customer_mail = Booking.objects.get(id=booking).customer.customer_email

            lines = ["Invoice","Thanks for the stay.","Regards","Abhishek Kumar"]

            pdf_buffer = generate_pdf(lines)

            # Create the email
            email = EmailMessage(
                "Hotel Booking App",
                "Your booking has been confirmed",
                settings.EMAIL_HOST_USER,
                [customer_mail],
            )

            # Attach the PDF
            email.attach('booking_confirmation.pdf', pdf_buffer.getvalue(), 'application/pdf')

            # Send the email
            email.send(fail_silently=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class Check_outUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Check_out.objects.get(id=id)
        except Check_out.DoesNotExist:
            return None


    def put(self, request, id):
 
        Check_out_instance = self.get_object(id)
        if not Check_out_instance:
            return Response(
                {"res": "Object with Check out id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data
        booking = data.get("booking")
        check_in = data.get("check_out")


        data = {
            "booking" : booking,
            "check_out" : check_out,
        }

        serializer = Check_outSerializer(instance = Check_out_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Check_outDeleteByIdApiView(APIView):    
    
    def get_object(self, id):

        try:
            return Check_out.objects.get(id=id)
        except Check_out.DoesNotExist:
            return None

    def delete(self, request, id):
        Check_out_instance = self.get_object(id)
        if not Check_out_instance:
            return Response(
                {"res": "Object with Check out id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        Check_out_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
