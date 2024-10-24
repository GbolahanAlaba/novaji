from django.urls import path, include
from . views import *



urlpatterns = [
   path('register/', RegisterViewSets.as_view({"post": "register"}), name='register'),
   path('get-registrations/', RegisterViewSets.as_view({"get": "get_registrations"}), name='registrations-get'),
   path('update-registration/<str:ref_code>/', RegisterViewSets.as_view({"put": "update_registration"}), name='registration-update'),


]

"""write a python program that encrypt and decrpyt a text string "Welcome to Lagos" using the AES/256/CBC/PKCS7Padding algorithm from the cryptography library"""