from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # You can add custom fields here if needed
    # For example: my_field = forms.CharField()
    pass