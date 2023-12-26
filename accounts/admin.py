from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Agent

User = get_user_model()

class AgentConfig(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.agent:
            obj.agent = request.user
        super().save_model(request, obj, form, change)

admin.site.register(User)
admin.site.register(Agent, AgentConfig)
