from django.urls import path
from .views import (CustomerGetApiView,CustomerAddApiView,CustomerGetByIdApiView,CustomerUpdateByIdApiView,CustomerDeleteByIdApiView)

urlpatterns = [
    path('getAllCustomers', CustomerGetApiView.as_view()),
    path('addCustomer', CustomerAddApiView.as_view()),
    path('getCustomerById/<int:id>', CustomerGetByIdApiView.as_view()),
    path('updateCustomerById/<int:id>', CustomerUpdateByIdApiView.as_view()),
    path('deleteCustomerById/<int:id>', CustomerDeleteByIdApiView.as_view())
]