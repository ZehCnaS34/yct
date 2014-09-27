from django.conf.urls import patterns, url

from annuals import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^(?P<annual_id>\d+)/sign/$', views.sign, name='sign'),
                       url(r'^(?P<continue_id>\d+)/sign/$', views.sign, name='sign'),
)
