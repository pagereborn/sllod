from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Poll.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sllod/', include('sllod.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^', include("home.urls")),
    
)

