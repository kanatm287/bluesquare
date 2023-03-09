from django import forms
from .models import Client, Insurance


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'full_name': 'Full name',
            'gender': 'Gender',
            'birth_date': 'Birth date',
            'address': 'Address'
        }


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'
        widgets = {'client': forms.HiddenInput()}
        labels = {
            'insurance_id': 'Insurance number',
            'insurance_type': 'Insurance type',
            'start_date': 'Start date',
            'end_date': 'End date'
        }
