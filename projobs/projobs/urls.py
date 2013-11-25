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
    url(
        r'^vagas/',
        include('vagas.urls', namespace='vagas')
    ),

    url(r'^login/$', 'django.contrib.auth.views.login', {
            'template_name': 'login.html'
        }, name='login'
    ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
            'template_name': 'logout.html', 'next_page': '/'
        }, name='logout'
    ),

    url(r'^admin/', include(admin.site.urls)),
)
