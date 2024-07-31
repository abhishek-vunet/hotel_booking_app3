from .models import Hotel,Review
from customer.models import Customer
from .serializers import HotelSerializer,ReviewSerializer

from rest_framework import status # for http status
from rest_framework.response import Response 
from rest_framework.views import APIView #to define the apis


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
    
