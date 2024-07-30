from .models import Student
from .serializers import StudentSerializer

from rest_framework import status # for http status
from rest_framework.response import Response 
from rest_framework.views import APIView #to define the apis


class StudentListApiView(APIView):

    def get(self, request):
        '''
        List all the student items for given requested user
        '''
        # print(request.user)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # This is for conditional authentication
    def post(self, request):
        '''
        Create the student with given student data
        '''
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

        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailApiView(APIView):

    def get_object(self, student_id):
        '''
        Helper method to get the object with given student_id
        '''
        try:
            return Student.objects.get(id=student_id)
        except Student.DoesNotExist:
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

        serializer = StudentSerializer(student_instance)
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

        serializer = StudentSerializer(instance = student_instance, data=data, partial = True)
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