from django.db import models
from django.conf import settings
from .choices import *

# Create your models here.
class World(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Guild(models.Model):
    name = models.TextField(max_length=255)
    is_owner = models.NullBooleanField()
    world = models.ForeignKey(World, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Vocation(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    level = models.IntegerField()
    vocation = models.ForeignKey(Vocation, on_delete=models.CASCADE)
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.level)

class Event(models.Model):
    name = models.TextField(max_length=255)
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    date = models.DateTimeField()
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Slot(models.Model):
    required_vocation = models.ForeignKey(Vocation, on_delete=models.CASCADE, blank=True, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name


