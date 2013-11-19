from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomeView
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(
        r'^profissionais/',
        include('profissionais.urls', namespace='profissionais')
    ),
    url(
        r'^empresas/',
        include('empresas.urls', namespace='empresas')
    ),

    url(r'^admin/', include(admin.site.urls)),
)
