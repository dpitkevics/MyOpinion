from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from Users import views


urlpatterns = patterns('',
                       url(r'^register$', views.RegisterView.as_view(), name='register'),
                       url(r'^login$', views.LoginView.as_view(), name='login'),
                       url(r'^register/success/$', TemplateView.as_view(template_name='Users/register_success.html'),
                           name='register_success'),
                       url(r'^logout/$', views.logout_view, name='logout'),
                       )