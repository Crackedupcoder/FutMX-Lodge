from django.contrib import sitemaps
from django.urls import reverse
from .models import Lodge, Room

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact','rooms','lodges']  # Add other URL names as needed

    def location(self, item):
        return reverse(item)
    
class LodgeSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Lodge.objects.all()
    

class RoomSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Room.objects.all()
    