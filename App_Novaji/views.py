from django.shortcuts import render
from rest_framework import viewsets
from . serializers import *
from . utils import *
from rest_framework import status
# Create your views here.


class RegisterViewSets(viewsets.ViewSet):
    serializer_class = RegisterSerializer   

    @handle_exceptions
    def register(self, request):

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
        obj = Register.objects.filter(reg_id=reg_id)

        serializer = self.serializer_class(obj, many=True)
        serializer = self.serializer_class(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"status": "success", "message": "Record updated", "data": serializer.data}, status=status.HTTP_200_OK)