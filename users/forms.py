from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from phonenumber_field import modelfields


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password1', 'password2']

    def save(self, *args, **kwargs):
        super(UserRegistrationForm, self).save(*args, **kwargs)
