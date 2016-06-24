from django.db import models
from django.utils import timezone ,datetime_safe
from datetime import datetime
from django import forms

"""
class RegistrationForm(forms.Form):
    Email = forms.CharField(label = '아이디', max_length = 40)
    password = forms.CharField(label = '비밀번호', widget = forms.Password-nput())
    firstname = models.CharField(max_length = 10)
    lastname = models.CharField(max_length = 10)
"""    
class info_client(models.Model):
    firstname = models.CharField(max_length = 10)
    lastname = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100)
    join_date = models.DateField(null=False,
        default = datetime_safe.date.today)  
    text = models.TextField(null=True)
    
    def submit(self):
        self.save()
    def __str__(self):
        return self.firstname

