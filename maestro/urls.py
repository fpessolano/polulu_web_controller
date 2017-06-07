from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /maestro/
    url(r'^$', views.index, name='index'),
    # ex: /maestro/5/
    url(r'^(?P<channel_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /add
    url(r'^add', views.newchannel, name='newchannel'),
    url(r'^delete/(?P<channel_id>[0-9]+)/$', views.deletechannel, name='deletechannel')     
]