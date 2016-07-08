from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getplayers/', views.get_players, name='get_players'),
    url(r'^addplayer/', views.add_player, name='add_player')
]
