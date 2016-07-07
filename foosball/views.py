from django.core import serializers
from django.http import JsonResponse
from foosball.models import Player
import json

def index(request):
    players = Player.objects.all()
    return JsonResponse(json.loads(serializers.serialize('json', players)), safe=False)
