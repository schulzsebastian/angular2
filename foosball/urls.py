from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getplayers/', views.index, name='index')
]
