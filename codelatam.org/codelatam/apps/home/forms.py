__author__ = 'alex'
from django import forms

class sendInformationFORM(forms.Form):
        nombre = forms.CharField(label='Nombre',widget=forms.TextInput)
        email = forms.EmailField(label='email',widget=forms.TextInput)

