from django.contrib import admin
from .models import Character, World, Vocation, Event, Slot

# Register your models here.
admin.site.register(Character)
admin.site.register(World)
admin.site.register(Vocation)
admin.site.register(Event)
admin.site.register(Slot)
