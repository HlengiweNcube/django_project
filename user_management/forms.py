from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


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