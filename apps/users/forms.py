from dataclasses import fields
from black import err
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        models = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        models = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"