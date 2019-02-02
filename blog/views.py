from django.shortcuts import render
from django.http import *
from .models import Destination

from django.db.models import Q

from .forms import DurationForm

from math import sin, cos, sqrt, atan2, radians

import collections
# Create your views here.

#find common destinatioin
# def unique_list(list):
#     print('ok')
# 	multiple_item=[]
#
# 	for item in list:
# 		count = list.count(item)
# 		if(count>1):
# 			print(item)
# 			multiple_item.append(item)
# 			list.remove(item)
# 	return multiple_item
    # uniq_list = []
    # uniq_set = set()
    # for item in list:
    #    if item not in uniq_set:
    #         uniq_list.append(item)
    #         uniq_set.add(item)
    # return uniq_list

#duplicate
def unique_list(list1):
    print('ok')
    toto = list(list1)
    multiple_item = []
    print(type(toto))
    print(toto)
    print('hera')
    print(list1)
    return multiple_item
    # for item in list1:
    #     print('kokokokoko')
    #     print(item)
    #     count = list.count(item)
    #     if(count>1):
    #         print(item)
    #         multiple_item.append(item)
    #         list.remove(item)
    # return multiple_item


#filter plaes radio TextInput
def FilterPlacesRadioInput(send):
    places = Destination.objects.filter(
    Q(trekking_type__contains = send['trekking']), Q(destinaton_type__contains = send['destination']), Q(accomodation_type__contains = send['accomodation'])
    )
    radiofilterplace = []
    for p in places:
        radiofilterplace.append(p.title)
    print(radiofilterplace)
    return radiofilterplace


#function to filter places
def FilterPlaces(send):

    toto = send['trekking'];
    # koko = list(toto.split(","));

    # print(type(koko))
    #
    # print(koko[1])

    # koba = list(toto)
    # print(type(koba))

    new = toto.replace('[', '')
    new1 = new.replace(']', '')
    # new2 = new1.replace(',', '')
    new3 = new1.replace("'", '')
    # new4 = new3.replace(' ', '')
    new4 = list(new3.split(","))

    print(type(new4))
    print(new4)


    # print(new3)
    # print(trek)
    # print(type(trek))





    # str1 = ''.join(map(str, toto))
    # ", ".join(map(str, alist))
    # print(str1)
    # print(toto)
    # for i in toto:
    # mardim = Destination.objects.all()
    # if cycling checkbox is checked:
    #     mardim = mardim.filter(trekking_type='Cycling')
    # if walking checkbox is checked:
    #     mardim = mardim.filter(trekking_type='Walking')
    # mardim = Destination.objects.filter(
    #     Q(trekking_type__contains=hami)
    #         )
    # mardim = {}

    # for i in range(len(trek)):
        # value
    store = []
    for trek in new4:
        if 'Walking' in trek:
            value4 = Destination.objects.filter(
            Q(trekking_type__contains="Walking")
            )
            print(type(value4))
            print('waking')
            print(set(value4))
            store.append(value4)

        if 'Cycling' in trek:
            value5 = Destination.objects.filter(
            Q(trekking_type__contains="Cycling")
            )
            print('cycling')
            print(value5)
            store.append(value5)
        if 'Biking' in trek:
            value6 = Destination.objects.filter(
            Q(trekking_type__contains="Biking")
            )
            print('biking')
            print(value6)
            store.append(value6)
        if 'Peak Climbing' in trek:
            value7 = Destination.objects.filter(
            Q(trekking_type__contains="Peak Climbing")
            )
            store.append(value7)
        if 'Others' in trek:
            value8 = Destination.objects.filter(
            Q(trekking_type__contains="Others")
            )
            store.append(value8)

    # gobo = Destination.objects.filter(
    # Q(trekking_type__contains="Cycling")
    # )
    # print(mardim)
    # ram = set(mardim).intersection(value5)
    print('store')
    print(store)
    trekking_filtered = unique_list(store)
    print('here')
    print(trekking_filtered)
    # seen = set()
    # seen_add = seen.add
    # seen_twice = set(x for x in store if x in seen or seen_add(x))

    # print('here')
    # print(seen_twice)



    # try:


    print('gogogoo')

    # print(ram)
    # print(gobo)
    # print(mardim)
    #
    # # for i in len(trek)
    #
    # print(mardim)

    # print(mardim)
    # print(trekking)
    # i = len(send['trekking'])
    # for trek in send['trekking']:

    # cheese_blog = Blog.objects.get(name="Cheddar Talk")
    # for trek in




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
            data = []
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
                    data.append(name)

            send = {'trekking':trekking, 'destination': destination, 'accomodation': accomodation}

            filteredplaces = FilterPlacesRadioInput(send)
            common = set(data).intersection(set(filteredplaces))
            finaldestination = Destination.objects.filter(title__in = common)
            gogo = {'places': finaldestination}
            return render(request, 'blog/r_result.html', gogo)
    else:
        form = DurationForm()
    return HttpResponseRedirect('/recommendation/')


def post(request):
    return render(request, 'blog/post.html')
