from django.shortcuts import render, redirect
from .models import Agent
from lodges.models import Room
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import AgentContactForm
from django.core.mail import send_mail
from lodges.models import Room, Lodge
from lodges.views import price_choices
from django.contrib import messages


def agents_list(request):
    agents_query = Agent.objects.all()
    agents_per_page = 9
    paginator = Paginator(agents_query, agents_per_page)
    page_number = request.GET.get('page', 1)
    try:
        agents = paginator.page(page_number)
    except EmptyPage:
        agents = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        agents = paginator.page(1)
    cxt = {'agents':agents,
            'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices,
            'price_choices': price_choices,
            'values':request.GET,}
    return render(request, 'account/agents.html', cxt)


def agent_detail(request, pk):
    agent = Agent.objects.get(agent__username=pk)
    agent_rooms = Room.objects.filter(agent=agent)
    room_count = agent_rooms.count()
    if request.method == 'POST':
        form = AgentContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} with email {cd['email']}"
            message = f"{cd['message']}"
            to = agent.agent.email
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            print(f"To: {to}")
            send_mail(subject, message, 'futmxlodge@gmail.com', [to])
            messages.success(request, "Your Message has been Successfully Sent The Agent Would get back to you as Soon as Possible, If you want a Quicker response Please Contact via Phone or Any of their Social Media Pages")
        else:
            messages.error(request, "Please Try Again")
    else:
        form = AgentContactForm()
    cxt = {'agent':agent, 'agent_rooms':agent_rooms, 
           'room_count':room_count,
            'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices,
            'price_choices': price_choices,
            'values':request.GET,}
    return render(request, 'account/agent.html', cxt)