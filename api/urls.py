from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plan/(?P<pid>[0-9]+)$', views.plan_by_id, name='plan_by_id'),
    url(r'^user/(?P<uid>[0-9]+)$', views.user_by_id, name='user_by_id')
]