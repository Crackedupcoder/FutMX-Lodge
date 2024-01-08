from django.contrib import admin
from .models import Lodge, Room, RoomImage, LodgeImage, LodgeAmmenities


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 4


class LodgeImageInline(admin.TabularInline):
    model = LodgeImage
    extra = 4


class LodgeAmmenitiesInline(admin.TabularInline):
    model = LodgeAmmenities
    extra = 4


class LodgeConfig(admin.ModelAdmin):
    search_fields = ('name','campus', 'area',)
    list_display = (
        'name','campus', 'area','light','water',
    )
    list_filter = (
        'campus', 'area', 'light', 'water',
    )
    fieldsets = (
        (None,{'fields':('name','campus','price','area','light','water','cover_image','available_rooms','description')}),
    )
    inlines = [LodgeImageInline, LodgeAmmenitiesInline]


class RoomConfig(admin.ModelAdmin):
    search_fields = ('lodge','type', 'number',)
    list_display = (
        'lodge','agent', 'type', 'lodge_light','lodge_water', 'lodge_campus'
    )
    list_filter = (
        'type','agent','lodge__light','lodge__water','lodge__campus',
    )
    inlines = [RoomImageInline]
    autocomplete_fields = ('lodge',)
    fieldsets = (
        (None,{'fields':('lodge','type','number','block','cover_image','price','video', 'availabe')}),
    )

    def save_model(self, request, obj, form, change):
        # Set the 'agent' field to the currently logged-in user
        obj.agent = request.user.agent
        super().save_model(request, obj, form, change)

    def lodge_campus(self, obj):
        return obj.lodge.get_campus_display() 

    lodge_campus.short_description = 'Lodge Campus'

    def lodge_water(self, obj):
        return obj.lodge.get_water_display() 

    lodge_water.short_description = 'Lodge Water'

    def lodge_light(self, obj):
        return obj.lodge.get_light_display() 
    
    lodge_light.short_description = 'Lodge Light'

admin.site.register(Lodge, LodgeConfig)
admin.site.register(Room, RoomConfig)

