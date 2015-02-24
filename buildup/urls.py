from django.conf.urls import patterns, url
from buildup.models import Fact
urlpatterns = patterns('',
  url(r'^$', 'buildup.views.hello', name='hello'),
  url(r'^time/$', 'buildup.views.time', name='time'),
  url(r'^rand/$', 'buildup.views.rand', name='rand'),
  url(r'^hello/(?P<yourname>.+)/$', 'buildup.views.helloname', name='yourname'),
  url(r'^speak/(?P<speak>.+)/$', 'buildup.views.speaks', name='speak' ),
  url(r'^hello_template/(?P<yourname>\w+)/$', 'buildup.views.hello_template', name='hello_template'),
  url(r'^rand_template/$', 'buildup.views.rand_template', name='rand_template'),
  url(r'^facts/$', 'buildup.views.all_facts', name='all_facts'))