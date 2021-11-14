from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class StaffCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')
    class Meta:
        model = User
        fields = [
            "is_customer",
            "is_dispatcher",
            "is_team_lead",
            "is_driver",
            "username",
            "email",
            "password1",
            "password2",
        ]
