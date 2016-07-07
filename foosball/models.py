from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(null=False, max_length=200)
    points = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
