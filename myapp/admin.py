from django.contrib import admin
from .models import Agent
# Register your models here.
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    # list_display = ('agent_name', 'provider','firstMessage', 'created_at')
    # search_fields = ('agent_name',)
    # list_filter = ('provider',)
    # ordering = ('-created_at',)
    class Meta:
        model = Agent
        fields = '__all__'
    

