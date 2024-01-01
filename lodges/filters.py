import django_filters
from .models import Room, Lodge

class RoomFilter(django_filters.FilterSet):
    campus = django_filters.CharFilter(field_name='lodge__campus', lookup_expr='iexact')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    room_type = django_filters.CharFilter(field_name='type', lookup_expr='iexact')
    area = django_filters.CharFilter(field_name='lodge__area', lookup_expr='icontains')
    water = django_filters.CharFilter(field_name='lodge__water', lookup_expr='iexact')
    light = django_filters.CharFilter(field_name='lodge__light', lookup_expr='iexact')

    class Meta:
        model = Room
        fields = []
