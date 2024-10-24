from django.contrib.auth.models import User
from . models import *
from rest_framework.response import Response
from rest_framework import serializers, validators



    
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Register
        fields = ['phone_number', 'mobile_network', 'ref_code']
    

