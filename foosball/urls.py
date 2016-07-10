from django.conf.urls import url
from . import views, api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getplayers/', api.get_players, name='get_players'),
    url(r'^addplayer/', api.add_player, name='add_player'),
    url(r'^addpoints/', api.add_points, name='add_points')
]
