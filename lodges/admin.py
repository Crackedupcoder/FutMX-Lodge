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
    prepopulated_fields = {'slug': ('name',)}
    add_fieldsets = (
        ( {
            'classes': ('wide',),
            'fields': ('name','campus','area','light','water','cover_image','available_rooms')
        },),
    )
    inlines = [LodgeImageInline, LodgeAmmenitiesInline]


class RoomConfig(admin.ModelAdmin):
    search_fields = ('lodge','type', 'number',)
    list_display = (
        'lodge', 'type', 'number','block', 'lodge_campus'
    )
    list_filter = (
        'type',
    )
    prepopulated_fields = {'slug': ('lodge',)}
    inlines = [RoomImageInline]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('agent','lodge','price',)
        },),)
    def lodge_campus(self, obj):
        return obj.lodge.get_campus_display() # Assuming 'campus' is a CharField in the Lodge model

    lodge_campus.short_description = 'Lodge Campus'

admin.site.register(Lodge, LodgeConfig)
admin.site.register(Room, RoomConfig)


# class UserAccountConfig(UserAdmin):
#     ordering = ('-created_at',)
#     search_fields = ('email','first_name','last_name')
#     list_display = (
#         'email','first_name','last_name','is_staff','is_active'
#     )
#     fieldsets = (
#         (None,{'fields':('username','email','first_name','last_name','about','avatar','skills')}),
#         ('Permissions', {'fields': ('is_staff','is_active','is_superuser',)})
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username','email','first_name','password1','password2','is_staff','is_superuser')
#         },),
#     )


# class CreatorAccountConfig(admin.ModelAdmin):
#     search_fields = ('creator',)
#     list_display = (
#         'creator',
#     )
#     fieldsets = (
#         (None,{'fields':('creator',)}),
#         ('Permissions', {'fields': ('is_verified',)})
#     )