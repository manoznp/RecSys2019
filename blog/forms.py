
from django import forms

DURATION_CHOICES = [
    ('100', '1-2 days of trek'),
    ('250', '3-7 days of trek'),
    ('450', '8-14 days of trek'),
    ('600', '15-20 days of trek'),
    ('1000', '20+ days of trek'),

]

TREKKING_CHOICES = [
    ('Cycling', 'Cycling'),
    ('Walking', 'Walking'),
    ('Biking', 'Biking'),
    ('Peak Climbing', 'Peak Climbing'),
    ('Others', 'Others'),
]

DESTINATION_CHOICES = [
    ('Adventure', 'Adventure'),
    ('Pilgrims', 'Pilgrims'),
    ('Waterbody', 'Waterbody'),
    ('Himalayas', 'Himalayas'),
    ('Nature Seeing', 'Nature Seeing'),
    ('Others', 'Others'),
]

ACCOMODATION_CHOICES = [
    ('Hotel', 'Hotel'),
    ('Pilgrims', 'Pilgrims'),
    ('Teahouse', 'Teahouse'),
    ('Motel', 'Motel'),
    ('Tent', 'Tent'),
    ('Homestay', 'Homestay'),
]

class DurationForm(forms.Form):
    duration = forms.CharField(
    widget=forms.RadioSelect(choices=DURATION_CHOICES, attrs={'class' : 'form-group radio_input icheck required'}))
    latitude = forms.FloatField(label='latitude')
    longitude = forms.FloatField(label='longitude')

     # myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
     # form.fields['field_name'].widget = forms.HiddenInput()

    trekking_type = forms.CharField(
    widget=forms.CheckboxSelectMultiple(choices=TREKKING_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))
    
    destination_type = forms.CharField(
    widget=forms.CheckboxSelectMultiple(choices=DESTINATION_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))

    accomodation_type = forms.CharField(
    widget=forms.CheckboxSelectMultiple(choices=ACCOMODATION_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))
