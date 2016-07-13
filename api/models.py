from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start = models.DateField(blank=False)
    final = models.DateField(blank=False)