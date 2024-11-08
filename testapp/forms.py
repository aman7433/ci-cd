from django import forms
from .models import modeldata

class formsdata(forms.ModelForm):
    class Meta:
        model=modeldata
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }