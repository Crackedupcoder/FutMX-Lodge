from django import forms
from .models import Lodge

class LodgeAddForm(forms.ModelForm):
    class Meta:
        model = Lodge
        fields = ['name','area','campus','light','water','cover_image','available_rooms',]
