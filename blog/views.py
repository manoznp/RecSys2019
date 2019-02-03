from django.shortcuts import render
from django.http import *
from .models import Destination

from django.db.models import Q

from .forms import DurationForm

from math import sin, cos, sqrt, atan2, radians

from scipy import spatial

# import collections
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


def ApplyCosineSimi(cosine_para, places):
    print(cosine_para)
    allnumlist = [int(x) for x in cosine_para]
    print(allnumlist)
    data = Destination.objects.filter(title__in = places)
    result1=[]
    for d in data:
        place = [d.temperature, d.altitude, d.difficulty, d.security]
        print(place)
        result = (1 - spatial.distance.cosine(place, allnumlist)) * 100
        result1.append(float("{0:.2f}".format(result)))
        # g = float("{0:.2f}".format(x))
    print(result1)
    return result1
        #temperature, altitude, difficulty, security
        # place.append(d.temperature)
        # place.append(d.altitude)
        # place.append(d.difficulty)
        # place.append(d.security)
        # place_data.append(place)

    # result = {}
    # for input1 in place_data:
    #     result{}
    #     result = 1 - spatial.distance.cosine(dataSetI, dataSetII)



#function to filter places
def FilterPlaces(send):

    toto = send['trekking'];

    new = toto.replace('[', '')
    new1 = new.replace(']', '')
    # new2 = new1.replace(',', '')
    new3 = new1.replace("'", '')
    # new4 = new3.replace(' ', '')
    new4 = list(new3.split(","))

    print(type(new4))
    print(new4)

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
            print('okmana')
            temperature = form.cleaned_data['temperature']
            altitude = form.cleaned_data['altitude']
            difficulty = form.cleaned_data['difficulty']
            security = form.cleaned_data['security']
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
            #temperature, altitude, difficulty, security
            data_for_cosine = [temperature, altitude, difficulty, security]
            # {'temperature': temperature, 'altitude': altitude, 'difficulty': difficulty, 'security': security}
            print(data_for_cosine)
            filteredplaces = FilterPlacesRadioInput(send)

            common = set(data).intersection(set(filteredplaces))

            cosine_data = ApplyCosineSimi(data_for_cosine, common)
            finaldestination = Destination.objects.filter(title__in = common)

            gogo = {'places': finaldestination, 'cosine': cosine_data}

            return render(request, 'blog/r_result.html', gogo)
    else:
        form = DurationForm()
    return HttpResponseRedirect('/recommendation/')


def post(request):
    return render(request, 'blog/post.html')
