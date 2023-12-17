# business/forms.py
from django import forms

class BusinessSearchForm(forms.Form):
    business_name = forms.CharField(required=False, max_length=255, label='Business Name')
    address = forms.CharField(required=False, max_length=255, label='Address')
