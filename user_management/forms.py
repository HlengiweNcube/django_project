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
        labels = {
            'username': 'Username',
            'email': 'Email address',
            'password1': 'Password',
            'password2': 'Confirm password',
        }
        help_texts = {
            'username': 'Choose a unique username for logging in.',
            'email': 'Used for account communication and password reset.',
        }
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'username'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
            'password1': forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
            'password2': forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        }


class UpdateProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]
        labels = {
            'username': 'Username',
            'email': 'Email address',
            'first_name': 'First name',
            'last_name': 'Last name',
        }
        help_texts = {
            'first_name': 'Shown on the dashboard greeting when available.',
            'last_name': 'Shown on the dashboard greeting when available.',
        }
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'username'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
            'first_name': forms.TextInput(attrs={'autocomplete': 'given-name'}),
            'last_name': forms.TextInput(attrs={'autocomplete': 'family-name'}),
        }


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
        labels = {
            'phone_number': 'Phone number',
            'address': 'Street address',
            'city': 'City',
            'country': 'Country',
            'postal_code': 'Postal code',
        }
        help_texts = {
            'phone_number': 'Include the country code if applicable.',
            'postal_code': 'Enter the code used by your postal service.',
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'autocomplete': 'tel'}),
            'address': forms.TextInput(attrs={'autocomplete': 'street-address'}),
            'city': forms.TextInput(attrs={'autocomplete': 'address-level2'}),
            'country': forms.TextInput(attrs={'autocomplete': 'country-name'}),
            'postal_code': forms.TextInput(attrs={'autocomplete': 'postal-code'}),
        }