from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from .models import CustomUser, Profile

MOBILE_REGEX = "^(\+\d{1,3}[- ]?)?\d{10}$"

class UserRegistrationForm(UserCreationForm):
    phone = forms.IntegerField(
        required=True, 
        validators=[
            RegexValidator(
                regex=MOBILE_REGEX,
                message="Enter a valid mobile number",
                code="invalid_mobile",
            )
        ]
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email', 'password1', 'password2']

    def save(self, *args, **kwargs):
        super(UserRegistrationForm, self).save(*args, **kwargs)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']