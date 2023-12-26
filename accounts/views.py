from django.shortcuts import render
from .models import Agent
from lodges.models import Room


def agents_list(request):
    agents = Agent.objects.all()
    cxt = {'agents':agents}
    return render(request, 'account/agents-grid.html', cxt)


def agent_detail(request, pk):
    agent = Agent.objects.get(agent__username=pk)
    agent_rooms = Room.objects.filter(agent=agent)
    room_count = agent_rooms.count()
    cxt = {'agent':agent, 'agent_rooms':agent_rooms, 'room_count':room_count}
    return render(request, 'account/agent-single.html', cxt)