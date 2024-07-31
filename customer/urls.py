from django.urls import path
from .views import (CustomerGetApiView,CustomerAddApiView,CustomerGetByIdApiView,CustomerUpdateByIdApiView,CustomerDeleteByIdApiView)

urlpatterns = [
    path('getAllCustomers', CustomerGetApiView.as_view()),
    path('addCustomer', CustomerAddApiView.as_view()),
    path('getCustomerById/<int:customer_id>', CustomerGetByIdApiView.as_view()),
    path('updateCustomerById/<int:customer_id>', CustomerUpdateByIdApiView.as_view()),
    path('deleteCustomerById/<int:customer_id>', CustomerDeleteByIdApiView.as_view())
]