from django import forms

DURATION_CHOICES = [
    ('100', '1-2 days of trek'),
    ('250', '3-7 days of trek'),
    ('450', '8-14 days of trek'),
    ('600', '15-20 days of trek'),
    ('1000', '20+ days of trek'),
]

class DurationForm(forms.Form):
    duration = forms.CharField(
    widget=forms.RadioSelect(choices=DURATION_CHOICES, attrs={'class' : 'form-group radio_input icheck required'}))
    latitude = forms.FloatField(label='latitude')
    longitude = forms.FloatField(label='longitude')
     # myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
     # form.fields['field_name'].widget = forms.HiddenInput()
