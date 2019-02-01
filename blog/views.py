from django.shortcuts import render
from django.http import *
from .models import Destination

from .forms import DurationForm

from math import sin, cos, sqrt, atan2, radians
# Create your views here.

def HomePage(request):
    return render(request, 'blog/index.html')

def Recommendation(request):
    form = DurationForm()
    return render(request, 'blog/recommendation.html', {'form': form})

def r_result(request):
    if request.method == 'POST':
        form = DurationForm(request.POST)
        if form.is_valid():
            trekking = form.cleaned_data['trekking_type']
            destination = form.cleaned_data['destination_type']
            accomodation = form.cleaned_data['accomodation_type']
            places = Destination.objects.all()
            hamro = form.cleaned_data['duration']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            for place in places:
                R = 6373.0
                lat1 = radians(place.latitude)
                lon1 = radians(place.longitude)
                lat2 = radians(latitude)
                lon2 = radians(longitude)

                dlon = lon2 - lon1
                dlat = lat2 - lat1

                a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))

                distance = R * c

                print("Result:", distance)
                print("Should be:", 278.546, "km")

            gogo = {'hamro': hamro, 'lati': latitude, 'long': longitude, 'places': places, 'trekking': trekking, 'destination' : destination, 'accomodation' : accomodation}
            return render(request, 'blog/r_result.html', gogo)
    else:
        form = DurationForm()
    return HttpResponseRedirect('/recommendation/')
        # form = request.POST.get('DurationForm')
        # form.save()
        # print (form['durationi'])
        # return HttpResponseRedirect('/result/')
        # hamro = request.form['duration'].value()
        # hamro = request.POST.get['duration'].value()
    # else:
    #     form = DurationForm()
    # return render(request, 'blog/recommendation.html', {'form': form})

def post(request):
    return render(request, 'blog/post.html')
