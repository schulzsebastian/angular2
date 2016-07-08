from __future__ import print_function
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from foosball.models import Player
from foosball.serializers import PlayerSerializer


@api_view(['GET'])
def get_players(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_player(request):
    if request.method == 'POST':
        data = request.data.get('data')
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('New user: %s' % serializer.data['name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
