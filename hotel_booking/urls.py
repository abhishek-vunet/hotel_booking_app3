from django.urls import path
from .views import (CustomerListApiView,CustomerDetailApiView)

urlpatterns = [
    path('customers/', CustomerListApiView.as_view()),
    path('customers/<int:customer_id>/', CustomerDetailApiView.as_view()),
]