from django.urls import path
from . import views

urlpatterns = [
    path('agents/', views.agents_list, name='agents'),
    path('agent/<str:pk>/', views.agent_detail, name='agent'),
]
