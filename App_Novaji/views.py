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