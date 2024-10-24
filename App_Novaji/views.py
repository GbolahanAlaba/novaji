from django.shortcuts import render
from rest_framework import viewsets
from . serializers import *
from . utils import *
from rest_framework import status

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64


class RegisterViewSets(viewsets.ViewSet):
    serializer_class = RegisterSerializer   

    @handle_exceptions
    def register(self, request):
        phone = request.data.get("phone_number")

        is_valid_phone(phone)
        ref = generate_unique_code()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(ref_code=ref)
        return Response({"status": "success", "message": "Data registered successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    

    @handle_exceptions
    def get_registrations(self, request):
        obj = Register.objects.all()

        serializer = self.serializer_class(obj, many=True)
        return Response({"status": "success", "message": "Registered records", "data": serializer.data}, status=status.HTTP_200_OK)
    

    @handle_exceptions
    def update_registration(self, request, reg_id):
        obj = Register.objects.filter(reg_id=reg_id).first()

        if not obj:
            return Response({"status": "failed", "message": "Invalid registration ID"}, status=status.HTTP_404_NOT_FOUND)
        elif not reg_id:
            return Response({"status": "failed", "message": "Registration ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not request.data:
            return Response({"status": "failed", "message": "No data provided for update"}, status=status.HTTP_400_BAD_REQUEST)

        required_fields = ['phone_number', 'mobile_network', 'message']
        for field in required_fields:
            if field not in request.data:
                return Response({
                    "status": "failed", 
                    "message": f"'{field}' is a required field."
                }, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = self.serializer_class(obj, data=request.data)
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"status": "failed", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(updated_at=timezone.now())

        return Response({
            "status": "success", 
            "message": "Record updated successfully", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)