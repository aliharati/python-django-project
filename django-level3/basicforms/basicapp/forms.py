from django import forms
from django.core import validators

def check_z(value):
    if value[0] != 'z':

        raise forms.ValidationError("no Z")
class FormName(forms.Form):
    name = forms.CharField(validators=[check_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher=  forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

def clean_q(self):
    cd = self.cleaned_data['q']
    if not cd:
        raise forms.ValidationError("Please enter a search term.")
    return cd