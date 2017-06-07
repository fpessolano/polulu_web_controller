from django.contrib import admin

# Register your models here.

from .models import *

class ChannelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identifiers', {'fields': ['name', 'number']}),
        ('Constraints', {'fields': ['rangeMin', 'rangeMax']}),
        ('Dynamics', {'fields': ['speed', 'acceleration', 'target']}),
    ]
    list_display = ('name', 'number')
    
admin.site.register(Channel,ChannelAdmin)