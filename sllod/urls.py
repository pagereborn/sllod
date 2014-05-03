from django.conf.urls import patterns, url

from sllod import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
   # url(r'^create', views.add_poll, name='poll'),
    url(r'^add_poll/$', views.add_poll, name='add_poll'),
    url(r'^create_poll/$', views.create_poll, name='create_poll'),
    url(r'^get_polls/$', views.ajax_poll_list, name='get_poll'),
    url(r'^option_vote/$', views.option_vote, name='vote_poll'),
)