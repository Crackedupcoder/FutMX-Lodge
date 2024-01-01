from django.shortcuts import render
from lodges.models import Room, Lodge
from lodges.views import price_choices


def about(request):
    cxt = {'campus_choices': Lodge.Campus.choices,
            'type_choices': Room.RoomType.choices,
            'water_choices': Lodge.Water.choices,
            'light_choices': Lodge.Light.choices,
            'price_choices': price_choices,
            'values':request.GET,}
    return render(request, 'about/about.html', cxt)
