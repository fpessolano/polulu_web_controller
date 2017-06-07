from django.db import models

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(default=0)
    rangeMin = models.IntegerField(default=0)
    rangeMax = models.IntegerField(default=0)
    target = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    acceleration = models.IntegerField(default=0)
