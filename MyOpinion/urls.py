from django.conf.urls import include, url
from django.contrib import admin

from MyOpinion.settings import MEDIA_ROOT

urlpatterns = [
    # Examples:
    # url(r'^$', 'MyOpinion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Topics.urls', namespace='Topics')),
    url(r'^user/', include('Users.urls', namespace='Users')),
    url(r'^comments/', include('Comments.urls', namespace='Comments')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.+)$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
]
