from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('room/<slug:lodge>/', views.room_detail, name='room'),
    path('rooms/', views.room_list, name='rooms'),
    path('lodges/', views.lodge_list, name='lodges'),
    path('lodge/<slug:name>/', views.lodge_detail, name='lodge'),

]