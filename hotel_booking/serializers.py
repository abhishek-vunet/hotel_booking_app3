from rest_framework.serializers import ModelSerializer
from .models import Customer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id','first_name','last_name','customer_phone','customer_email') 
