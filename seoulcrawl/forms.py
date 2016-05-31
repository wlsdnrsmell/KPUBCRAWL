from django import forms
from .models import info_client

class info_client_Form(forms.ModelForm):
    class Meta:
        model = info_client
        fields = ('lastname','firstname','email','join_date','text')