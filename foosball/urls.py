from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getplayers/', views.get_players, name='get_players')
]
