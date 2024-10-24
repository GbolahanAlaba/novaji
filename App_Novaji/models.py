from django.db import models
import uuid

# Create your models here.


class Register(models.Model):
    reg_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=50, blank=True, null=True, default='')
    mobile_network = models.CharField(max_length=50, blank=True, null=True, default='')
    message = models.CharField(max_length=50, blank=True, null=True, default='')
    ref_code = models.CharField(max_length=100, blank=True, null=True, default="", unique=True)