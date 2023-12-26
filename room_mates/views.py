from django.shortcuts import render, redirect
from .models import RoomMate
from django.contrib import messages



def room_mates_list(request):
    room_mates = RoomMate.objects.all()
    cxt = {'room_mates':room_mates,
           'level_choices': RoomMate.Level.choices,
           'religion_choices': RoomMate.Religion.choices}
    return render(request, 'room_mates/list.html', cxt)


def room_mate_create(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('name')
        if request.FILES:
            user.avatar = request.FILES.get('avatar')
        user.save()
        RoomMate.objects.create(
            user = request.user,
            department = request.POST.get('department'),
            level = request.POST.get('level'),
            religion = request.POST.get('religion'),
            about = request.POST.get('about')
        )
        messages.success(request, 'Profile Succesfully Created')
        return redirect('room-mates')

    cxt = {}
    return render(request, 'room_mates/create.html', cxt)

