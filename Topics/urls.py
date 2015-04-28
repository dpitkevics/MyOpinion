from django.conf.urls import patterns, url

from Topics import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^topic/(?P<slug>.+)/$', views.view_topic, name='view_opinion'),
                       url(r'^tag/(?P<slug>.+)/$', views.topics_by_tag, name='view_by_tag'),
                       url(r'^category/(?P<slug>.+)/$', views.topics_by_category, name='view_by_category'),
                       )