from django import forms
from .models import *

class SubscriberForm(forms.ModelForm):
    
    class Meta:
        model=Subscribers
        exclude=[""]
        widgets={
                "name":forms.TextInput(attrs={'placeholder':'Enter your name','name':'Name','id':'name','class':'form-control'}),
                "email":forms.TextInput(attrs={'placeholder':'email','name':'email','id':'email','class':'form-control'}),
                "phone":forms.TextInput(attrs={'placeholder':'phone','name':'phone','id':'phone','class':'form-control'}),
                  } 