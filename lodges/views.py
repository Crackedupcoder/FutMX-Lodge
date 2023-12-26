from django.shortcuts import render, get_object_or_404
from .models import Lodge,Room, RoomImage
from accounts.models import UserAccount, Agent


def home_page(request):
    rooms = Room.objects.all()
    agents = Agent.objects.all()   
    cxt = {'rooms': rooms,
            'agents':agents,
            'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices}
    return render(request, 'lodges/index1.html', cxt)


def room_detail(request,lodge):
    room = get_object_or_404(Room, slug=lodge)
    agent = UserAccount.objects.get(username=room.agent)
    cxt = {'room':room, 'agent':agent}
    return render(request, 'lodges/room-single.html', cxt)


def room_list(request):
    rooms = Room.objects.all()
    cxt = {'rooms':rooms}
    return render(request, 'lodges/rooms-grid.html', cxt)


def lodge_list(request):
    lodges = Lodge.objects.all()
    cxt = {'lodges': lodges,
                   'campus_choices': Lodge.Campus.choices,
        'type_choices': Room.RoomType.choices,
        'values':request.GET,}
    return render(request, 'lodges/lodges-grid.html', cxt)


def lodge_detail(request, name):
    lodge = get_object_or_404(Lodge, slug=name)
    cxt = {'lodge':lodge,}
    return render(request, 'lodges/lodge-single.html', cxt)


def search(request):
    qs = Room.objects.order_by('-created_at')

    if 'campus' in request.GET:
        campus = request.GET['campus']
        if campus:
            qs = qs.filter(lodge__campus__iexact=campus)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            qs = qs.filter(price__lte=price)
    
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            qs = qs.filter(type__iexact=type)
    
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            qs = qs.filter(lodge__area__icontains=area)

    if 'water' in request.GET:
        water = request.GET['water']
        if water:
            qs = qs.filter(lodge__water__iexact=water)
    
    if 'light' in request.GET:
        light = request.GET['light']
        if light:
            qs = qs.filter(lodge__light__iexact=water)
        
    cxt = {
        'campus_choices': Lodge.Campus.choices,
        'type_choices': Room.RoomType.choices,
        'water_choices': Lodge.Water.choices,
        'light_choices': Lodge.Light.choices,
        'qs':qs,
        'values':request.GET,
    }
    return render(request, 'lodges/search.html', cxt)
