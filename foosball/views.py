from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from foosball.models import Player
from foosball.serializers import PlayerSerializer
import json

@api_view(['GET'])
def get_players(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
