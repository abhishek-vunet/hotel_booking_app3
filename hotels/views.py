from .models import Hotel,Review,Room,Amenities
from customer.models import Customer
from .serializers import HotelSerializer,ReviewSerializer,RoomSerializer,AmenitiesSerializer

from rest_framework import status # for http status
from rest_framework.response import Response 
from rest_framework.views import APIView #to define the apis

class SearchHotelByNameApiView(APIView):
        
    def get(self,request,name):
        
        hotel_instance = Hotel.objects.all()
        result = []
        for hotel in hotel_instance:
            hotel_name = hotel.hotel_name
            if name.lower() in hotel_name.lower():
                serializer = HotelSerializer(hotel)
                result.append(serializer.data)
        
        if result:
            return Response(result, status=status.HTTP_200_OK)
   
        return Response(
                {"res": "Object with hotel name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )


class HotelGetApiView(APIView):

    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HotelGetByIdApiView(APIView):

    def get_object(self, id):
        try:
            return Hotel.objects.get(id=id)
        except Hotel.DoesNotExist:
            return None
        
    def get(self,request,id):
        hotel_instance = self.get_object(id)
        if not hotel_instance:
            return Response(
                {"res": "Object with hotel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = HotelSerializer(hotel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HotelAddApiView(APIView):
    
    def post(self, request):

        data=request.data
        hotel_name = data.get("hotel_name")
        hotel_phone = data.get("hotel_phone")
        hotel_email = data.get("hotel_email")
        hotel_description = data.get("hotel_description")

        data = {
            "hotel_name" : hotel_name,
            "hotel_phone" : hotel_phone,
            "hotel_email" : hotel_email,
            "hotel_description" : hotel_description 
        }

        serializer = HotelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

class HotelUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Hotel.objects.get(id=id)
        except Hotel.DoesNotExist:
            return None


    def put(self, request, id):
 
        hotel_instance = self.get_object(id)
        if not hotel_instance:
            return Response(
                {"res": "Object with hotel id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data
        hotel_name = data.get("hotel_name")
        hotel_phone = data.get("hotel_phone")
        hotel_email = data.get("hotel_email")
        hotel_description = data.get("hotel_description")

        data = {
            "id" : id,
            "hotel_name" : hotel_name,
            "hotel_phone" : hotel_phone,
            "hotel_email" : hotel_email,
            "hotel_description" : hotel_description 
        }

        serializer = HotelSerializer(instance = hotel_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDeleteByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Hotel.objects.get(id=id)
        except Hotel.DoesNotExist:
            return None

    def delete(self, request, id):
        hotel_instance = self.get_object(id)
        if not hotel_instance:
            return Response(
                {"res": "Object with hotel id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        hotel_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    
class ReviewGetApiView(APIView):

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReviewGetByIdApiView(APIView):

    def get_object(self, id):
        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            return None
        
    def get(self,request,id):
        review_instance = self.get_object(id)
        if not review_instance:
            return Response(
                {"res": "Object with Review id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ReviewSerializer(review_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReviewAddApiView(APIView):
    
    def post(self, request):

        data=request.data
        hotel_id = data.get("hotel_id")
        customer_id = data.get("customer_id")
        reviews = data.get("reviews")

        data = {
            "hotel" : hotel_id,
            "customer" : customer_id,
            "reviews" : reviews,
        }

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

class ReviewUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            return None


    def put(self, request, id):
 
        review_instance = self.get_object(id)
        if not review_instance:
            return Response(
                {"res": "Object with review id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data
        hotel_id = data.get("hotel_id")
        customer_id = data.get("customer_id")
        reviews = data.get("reviews")

        data = {
            "hotel" : hotel_id,
            "customer" : customer_id,
            "reviews" : reviews,
        }

        serializer = ReviewSerializer(instance = review_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDeleteByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            return None

    def delete(self, request, id):
        review_instance = self.get_object(id)
        if not review_instance:
            return Response(
                {"res": "Object with Review id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        review_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    
class RoomGetApiView(APIView):

    def get(self, request):
        reviews = Room.objects.all()
        serializer = RoomSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RoomGetByIdApiView(APIView):

    def get_object(self, id):
        try:
            return Room.objects.get(id=id)
        except Room.DoesNotExist:
            return None
        
    def get(self,request,id):
        room_instance = self.get_object(id)
        if not room_instance:
            return Response(
                {"res": "Object with Room id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RoomSerializer(room_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RoomAddApiView(APIView):
    
    def post(self, request):

        data=request.data
        room_number = data.get("room_number")
        hotel = data.get("hotel")
        description = data.get("room_description")

        data = {
            "room_number" : room_number,
            "hotel" : hotel,
            "room_description": description
        }

        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

class RoomUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Room.objects.get(id=id)
        except Room.DoesNotExist:
            return None


    def put(self, request, id):
 
        room_instance = self.get_object(id)
        if not room_instance:
            return Response(
                {"res": "Object with review id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data
        room_number = data.get("room_number")
        hotel = data.get("hotel")
        description = data.get("description")

        data = {
            "room_number" : room_number,
            "hotel" : hotel,
            "description": description
        }

        serializer = RoomSerializer(instance = room_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomDeleteByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Room.objects.get(id=id)
        except Room.DoesNotExist:
            return None

    def delete(self, request, id):
        room_instance = self.get_object(id)
        if not room_instance:
            return Response(
                {"res": "Object with Review id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        room_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    
class AmenitiesGetApiView(APIView):

    def get(self, request):
        reviews = Amenities.objects.all()
        serializer = AmenitiesSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AmenitiesGetByIdApiView(APIView):

    def get_object(self, id):
        try:
            return Amenities.objects.get(id=id)
        except Amenities.DoesNotExist:
            return None
        
    def get(self,request,id):
        amenities_instance = self.get_object(id)
        if not amenities_instance:
            return Response(
                {"res": "Object with Room id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AmenitiesSerializer(amenities_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AmenitiesAddApiView(APIView):
    
    def post(self, request):

        data=request.data
        room = data.get("room")
        ac = data.get("ac")
        number_of_beds = data.get("number_of_beds")
        balcony = data.get("balcony")
        flour_num = data.get("flour_num")

        data = {
            "room" : room,
            "ac" : ac,
            "number_of_beds": number_of_beds,
            "balcony": balcony,
            "flour_num": flour_num
        }

        serializer = AmenitiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

class AmenitiesUpdateByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Amenities.objects.get(id=id)
        except Amenities.DoesNotExist:
            return None


    def put(self, request, id):
 
        amenities_instance = self.get_object(id)
        if not amenities_instance:
            return Response(
                {"res": "Object with review id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data

        room = data.get("room")
        ac = data.get("ac")
        number_of_beds = data.get("number_of_beds")
        balcony = data.get("balcony")
        flour_num = data.get("flour_num")

        data = {
            "room" : room,
            "ac" : ac,
            "number_of_beds": number_of_beds,
            "balcony": balcony,
            "flour_num": flour_num
        }

        serializer = AmenitiesSerializer(instance = amenities_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AmenitiesDeleteByIdApiView(APIView):

    def get_object(self, id):

        try:
            return Amenities.objects.get(id=id)
        except Amenities.DoesNotExist:
            return None

    def delete(self, request, id):
        amenities_instance = self.get_object(id)
        if not amenities_instance:
            return Response(
                {"res": "Object with Review id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        amenities_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    