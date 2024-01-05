from django.shortcuts import render, get_object_or_404
from .models import Lodge,Room, RoomImage
from accounts.models import UserAccount, Agent
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from accounts.forms import AgentContactForm
from django.core.mail import send_mail
from django.contrib import messages


def home_page(request):
    rooms = Room.objects.all()[:5]
    agents = Agent.objects.all()   
    cxt = {'rooms': rooms,
            'agents':agents,
            'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices,
            'price_choices': price_choices,
            'values':request.GET,}
    return render(request, 'lodges/index.html', cxt)


def room_detail(request,lodge):
    room = get_object_or_404(Room, slug=lodge)
    agent = UserAccount.objects.get(username=room.agent)
    if request.method == 'POST':
        form = AgentContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} enquiry on {room.lodge.name}"
            message = f"{cd['message']} reply at {cd['email']}"
            to = agent.email
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            print(f"To: {to}")
            send_mail(subject, message, 'futmxlodge@gmail.com', [to])
            messages.success(request, "Your Message has been Successfully Sent The Agent Would get back to you as Soon as Possible, If you want a Quicker response Please Contact via Phone or Any of their Social Media Pages")
        else:
            messages.error(request, "An Error Occured please Try Again")
    else:
        form = AgentContactForm()
    cxt = {'room':room, 'agent':agent,'form':form,
            'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices,
            'price_choices': price_choices,
            'values':request.GET,}
    return render(request, 'lodges/room.html', cxt)


def room_list(request):
    room_query = Room.objects.order_by('-created_at')
    if 'campus' in request.GET:
        campus = request.GET['campus']
        if campus:
            room_query = room_query.filter(lodge__campus__iexact=campus)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            try:
                price = float(price)
                room_query = room_query.filter(price__lte=price)
            except ValueError:
                price = float('1000000')
                room_query = room_query.filter(price__lte=price)
    
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            room_query = room_query.filter(type__iexact=type)
    
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            room_query = room_query.filter(lodge__area__icontains=area)

    if 'water' in request.GET:
        water = request.GET['water']
        if water:
            room_query = room_query.filter(lodge__water__iexact=water)
    
    if 'light' in request.GET:
        light = request.GET['light']
        if light:
            room_query = room_query.filter(lodge__light__iexact=light)
    rooms_per_page = 9
    paginator = Paginator(room_query, rooms_per_page)
    page_number = request.GET.get('page', 1)
    try:
        rooms = paginator.page(page_number)
    except EmptyPage:
        rooms = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        rooms = paginator.page(1)
    cxt = {'rooms':rooms,
        'campus_choices': Lodge.Campus.choices,
        'type_choices': Room.RoomType.choices,
        'water_choices': Lodge.Water.choices,
        'light_choices': Lodge.Light.choices,
        'price_choices': price_choices,
        'values':request.GET,}
    return render(request, 'lodges/rooms.html', cxt)


def lodge_list(request):
    lodge_query = Lodge.objects.all()
    lodges_per_page = 9
    paginator = Paginator(lodge_query, lodges_per_page)
    page_number = request.GET.get('page', 1)
    try:
        lodges = paginator.page(page_number)
    except EmptyPage:
        lodges = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        lodges = paginator.page(1)
    cxt = {'lodges': lodges,
            'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices,
            'price_choices': price_choices,
            'values':request.GET,}
    return render(request, 'lodges/lodges.html', cxt)


def lodge_detail(request, name):
    lodge = get_object_or_404(Lodge, slug=name)
    if request.method == 'POST':
        form = AgentContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} enquiry on {lodge.name}, email = {cd['email']}"
            message = f"{cd['message']} reply {cd['email']}"
            send_mail(subject, message, 'futmxlodge@gmail.com',['futmxlodge@gmail.com'])
            messages.success(request, "Your Message has been Successfully Sent We Would get back to you as Soon as Possible, If you want a Quicker response Please Contact Us via Phone or Any of Our Social Media Pages")
        else:
            messages.error(request, "An Error Occured please Try Again")
    else:
        form = AgentContactForm()
    cxt = {'lodge':lodge, 'form':form,
            'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices,
            'price_choices': price_choices,
            'values':request.GET,}
    return render(request, 'lodges/lodge.html', cxt)


price_choices = {
    '50000':'NGN 50,000.00',
    '100000':'NGN 100,000.00',
    '150000':'NGN 150,000.00',
    '200000':'NGN 200,000.00',
    '250000':'NGN 250,000.00',
}
