
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
    widget=forms.RadioSelect(choices=TREKKING_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))

    destination_type = forms.CharField(
    widget=forms.RadioSelect(choices=DESTINATION_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))

    accomodation_type = forms.CharField(
    widget=forms.RadioSelect(choices=ACCOMODATION_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))
