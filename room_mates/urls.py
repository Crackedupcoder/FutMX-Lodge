from django.urls import path
from . import views

urlpatterns = [
    path('room-mates/', views.room_mates_list, name='room-mates'),
    path('room-mates/create/', views.room_mate_create, name='room-mates-create'),
]