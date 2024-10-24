from django.urls import path, include
from . views import *


urlpatterns = [
   path('register/', RegisterViewSets.as_view({"post": "register"}), name='register')

]