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
        print('Returned %s' % serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


@api_view(['UPDATE'])
def add_points(request):
    if request.method == 'UPDATE':
        data = request.data.get('data')
        try:
            player = Player.objects.get(id=data['id'])
            player.points += int(data['points'])
            player.games += 1
            player.save()
            print('%s points for %s' % (player.points, player.name))
            return Response(data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
