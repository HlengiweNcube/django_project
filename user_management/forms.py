from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import UserProfile


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UpdateProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]


class UpdateContactForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            'phone_number',
            'address',
            'city',
            'country',
            'postal_code',
        ]