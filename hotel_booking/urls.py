from django.urls import path
from .views import (StudentListApiView,StudentDetailApiView)

urlpatterns = [
    path('students/', StudentListApiView.as_view()),
    path('students/<int:student_id>/', StudentDetailApiView.as_view()),
]