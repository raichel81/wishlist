from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(label='Name: ', max_length=50)
    start_date = forms.DateField(required=True, widget=forms.SelectDateWidget())
    class Meta:
        model = User
        fields = ('name','username', 'start_date', 'password1', 'password2')