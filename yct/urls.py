from django.conf.urls import patterns, include, url
from django.contrib import admin

from yct import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'yct.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', views.index, name='root'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^annuals/', include('annuals.urls', namespace='annuals')))
