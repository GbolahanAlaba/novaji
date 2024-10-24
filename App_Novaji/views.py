from django.shortcuts import render
from rest_framework import viewsets
from . serializers import *
from rest_framework import status
# Create your views here.


class RegisterViewSets(viewsets.ViewSet):
    serializer_class = RegisterSerializer   

    @handle_exceptions
    def register(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "success", "message": "Data registered successfully"}, status=status.HTTP_201_CREATED)