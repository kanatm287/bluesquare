from django import forms

GENDER = (
    ('M', 'male'),
    ('F', 'female'),
    ('U', 'undecided')
)


class ClientFrom(forms.Form):
    full_name = forms.CharField(label='Full name', max_length=30, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    birth_date = forms.DateField(label='Birth date', required=True)
    address = forms.CharField(label='Address', max_length=100, required=True)


INSURANCE_TYPE = (
    ('L', 'life-insurance'),
    ('M', 'medical-insurance'),
    ('A', 'auto-insurance')
)


class InsuranceForm(forms.Form):
    insurance_id = forms.IntegerField(min_value=1000000, max_value=999999, required=True)
    insurance_type = forms.ChoiceField(choices=INSURANCE_TYPE, required=True)
    start_date = forms.DateField(label='Start date', required=True)
    end_date = forms.DateField(label='End date', required=True)
