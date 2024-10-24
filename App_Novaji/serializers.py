from django.contrib.auth.models import User
from . models import *
from rest_framework.response import Response
from rest_framework import serializers, validators



    
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Register
        fields = ['reg_id', 'phone_number', 'mobile', 'ref_code']
    

