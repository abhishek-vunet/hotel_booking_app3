from .models import Customer
from .serializers import CustomerSerializer

from rest_framework import status # for http status
from rest_framework.response import Response 
from rest_framework.views import APIView #to define the apis


class CustomerGetApiView(APIView):

    def get(self, requesst):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomerGetByIdApiView(APIView):

    def get_object(self, customer_id):
        try:
            return Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return None
        
    def get(self,request,customer_id):
        customer_instance = self.get_object(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Object with customer id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CustomerSerializer(customer_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomerAddApiView(APIView):
    
    def post(self, request):

        data=request.data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        customer_phone = data.get("customer_phone")
        customer_email = data.get("customer_email")

        data = {
            "first_name" : first_name,
            "last_name" : last_name,
            "customer_phone" : customer_phone,
            "customer_email" : customer_email
        }

        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)


class CustomerUpdateByIdApiView(APIView):

    def get_object(self, customer_id):

        try:
            return Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return None


    def put(self, request, customer_id):
 
        customer_instance = self.get_object(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Object with customer id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        customer_phone = data.get("customer_phone")
        customer_email = data.get("customer_email")

        data = {
            "customer_id" : customer_id,
            "first_name" : first_name,
            "last_name" : last_name,
            "customer_phone" : customer_phone,
            "customer_email" : customer_email
        }

        serializer = CustomerSerializer(instance = customer_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDeleteByIdApiView(APIView):

    def get_object(self, customer_id):

        try:
            return Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return None

    def delete(self, request, customer_id):
        customer_instance = self.get_object(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Object with customer id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        customer_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )