from django import forms
from .models import info_client
from datetime import datetime
        
class info_client_Form(forms.ModelForm):
    #firstname = forms.CharField(max_length=10, required = True)
    #lastname = forms.CharField(max_length=10)
    #email = forms.EmailField(required = True)
    #join_date = forms.DateField()
    #text = forms.CharField(max_length=200)
    class Meta:
      model = info_client
      fields = ('firstname','lastname','email','join_date','text')