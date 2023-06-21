from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('doctor', 'DOCTOR'),
    ('patient', 'PATIENT'),
)


class CustomUser(AbstractUser):
    address= models.TextField(null=True, blank=False)
    city= models.CharField(max_length=200, null=True, blank= False)
    pincode= models.IntegerField(null=True, blank=False)
    image= models.ImageField(upload_to='image', null=True, blank=True)
    role= models.CharField(max_length=10, choices=ROLE_CHOICES, default='doctor')