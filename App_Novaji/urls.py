from django.urls import path, include
from . views import *



urlpatterns = [
   path('register/', RegisterViewSets.as_view({"post": "register"}), name='register'),
   path('get-registrations/', RegisterViewSets.as_view({"get": "get_registrations"}), name='registrations-get'),
   path('update-registration/<str:reg_id>/', RegisterViewSets.as_view({"put": "update_registration"}), name='registration-update'),


   path('encrypt/', RegisterViewSets.as_view({"get": "encrypt"}), name='encrypt'),

]

"""write a python program that encrypt and decrpyt a text string "Welcome to Lagos" using the AES/256/CBC/PKCS7Padding algorithm from the cryptography library"""