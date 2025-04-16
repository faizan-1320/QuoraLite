from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply 'form-control' class to each field for proper Bootstrap styling
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assigning the 'form-control' class to each field
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add form-control class to each field in the form
        self.fields['profile_image'].widget.attrs.update({
            'class': 'form-control'  # Class for file input
        })
        self.fields['bio'].widget.attrs.update({
            'class': 'form-control'  # Class for text area
        })
