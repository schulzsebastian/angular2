from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plan/(?P<pid>[0-9]+)$', views.plan_by_id, name='plan_by_id'),
    url(r'^plans$', views.get_plans, name='get_plans'),
    url(r'^plans/(?P<uid>[0-9]+)$', views.plans_by_user, name='plans_by_user'),
    url(r'^user/(?P<uid>[0-9]+)$', views.user_by_id, name='user_by_id'),
    url(r'^users$', views.get_users, name='get_users')
]