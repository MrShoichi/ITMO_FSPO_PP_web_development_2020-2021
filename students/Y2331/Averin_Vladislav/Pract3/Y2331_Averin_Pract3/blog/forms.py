from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# creating a form
class CarOwnerForm(forms.ModelForm):
    # create meta class
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # specify model to be used

        model = CarOwner
  
        # specify fields to be used
        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
            "date_birth",
            "passport_number",
            "home_address",
            "nationality",
            "password",
        ]


class CarForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car

        # specify fields to be used
        fields = [
            "state_number",
            "mark",
            "model",
            "color",
        ]
