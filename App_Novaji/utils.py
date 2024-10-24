from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from . models import *
import random
import string


def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = str(e)
            return Response({"status": "failed", "message": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper




def generate_unique_code(length=16):
    characters = string.ascii_letters + string.digits
    unique_code = ''.join(random.choices(characters, k=length))
    return unique_code