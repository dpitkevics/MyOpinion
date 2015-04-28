from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'MyOpinion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Topics.urls', namespace='Topics')),
    url(r'^user/', include('Users.urls', namespace='Users')),
    url(r'^admin/', include(admin.site.urls)),
]
