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
            places = Destination.objects.all()
            hamro = form.cleaned_data['duration']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            data = {}
            for place in places:
                R = 6373.0
                name = place.title
                lat1 = radians(place.latitude)
                lon1 = radians(place.longitude)
                lat2 = radians(latitude)
                lon2 = radians(longitude)

                dlon = lon2 - lon1
                dlat = lat2 - lat1

                a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))

                distance = R * c

                if distance <= int(hamro):
                    data[name] = distance

            gogo = {'hamro':data}
            # 'rec':recommend,'rec':recommend,
            return render(request, 'blog/r_result.html', gogo)
    else:
        form = DurationForm()
    return HttpResponseRedirect('/recommendation/')


def post(request):
    return render(request, 'blog/post.html')
