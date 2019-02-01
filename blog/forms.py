from django import forms


# average trekkers walk 8 hour
# average walking speed 3.6 /hour
# 1 day 28.8 km



DURATION_CHOICES = [
    (60, '1-2 days of trek'),
    (201, '3-7 days of trek'),
    (403, '8-14 days of trek'),
    (576, '15-20 days of trek'),
    (1000, '20+ days of trek'),
]

class DurationForm(forms.Form):
    duration = forms.CharField(
    widget=forms.RadioSelect(choices=DURATION_CHOICES, attrs={'class' : 'form-group radio_input icheck required'}))
    latitude = forms.FloatField(label='latitude')
    longitude = forms.FloatField(label='longitude')
     # myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
     # form.fields['field_name'].widget = forms.HiddenInput()
