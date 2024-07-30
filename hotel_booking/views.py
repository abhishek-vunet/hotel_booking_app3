from .models import Customer
from .serializers import CustomerSerializer

from rest_framework import status # for http status
from rest_framework.response import Response 
from rest_framework.views import APIView #to define the apis


class CustomerListApiView(APIView):

    def get(self, requesst):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        Create the student with given student data
        '''
        data=request.data
        print(data)
        customer_id = data.get("customer_id")
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

        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailApiView(APIView):

    def get_object(self, student_id):
        '''
        Helper method to get the object with given student_id
        '''
        try:
            return Customer.objects.get(id=student_id)
        except Customer.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self,request,student_id):
        '''
        Retrieves the student with given student_id
        '''
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Object with student id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CustomerSerializer(student_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, student_id):
        '''
        Updates the student item with given student_id if exists
        '''
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Object with student id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data=request.data
        name = data.get("name")
        age = data.get("age")
        email = data.get("email")
        address = data.get("address")

        data = {
            'name': name,
            'age': age,
            'email':email,
            'address':address
        }

        serializer = CustomerSerializer(instance = student_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, student_id):
        '''
        Deletes the student item with given student_id if exists
        '''
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Object with student id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        student_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )