from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomeView
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    # Include example
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
