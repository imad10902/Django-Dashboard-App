from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from .models import CustomUser

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['image', 'username', 'role', 'first_name', 'last_name', 'email', 'address', 'city', 'pincode']

#form for user model with additional fields