# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from .views import AtivarView


urlpatterns = patterns('',
    url(
        r'^ativar/(?P<activation_key>[0-9a-f-]{36})/$',
        AtivarView.as_view(),
        name='ativar'
    ),
)
