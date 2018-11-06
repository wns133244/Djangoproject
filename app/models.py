from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import django.forms as forms


class Member(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True)
    user_mail = models.CharField(max_length=50)
    user_birth = models.CharField(max_length=50)
    c_date = models.DateTimeField()

class JoinForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user_name', 'user_mail', 'user_birth']
        widgets = {
            'user_name': forms.TextInput(),
            'user_mail': forms.TextInput(),
            'user_birth': forms.DateInput()
        }

class LoginForm(forms.ModelForm):
     class Meta:
         model = Member
         fields = ['user_name', 'user_mail']
         widgets = {
         'user_name': forms.Textarea(),
         'user_mail': forms.Textarea(),
         }

