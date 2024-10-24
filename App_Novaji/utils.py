from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from . models import *
import random
import string
import re
from rest_framework.exceptions import ValidationError

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = str(e)
            return Response({"status": "failed", "message": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper


def is_valid_phone(phone):
    NIGERIAN_PHONE_REGEX = re.compile(r'^(?:\+234|0)?(?:70|80|81|90|91|70|71)\d{8}$')
    if not NIGERIAN_PHONE_REGEX.match(phone):
        raise ValidationError({"status": "failed", "message": "Invalid phone number"})
    return True

def generate_unique_code(length=16):
    characters = string.ascii_letters + string.digits
    unique_code = ''.join(random.choices(characters, k=length))
    return unique_code