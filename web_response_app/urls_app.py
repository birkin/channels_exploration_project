# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url
from django.views.generic import RedirectView
from web_response_app import views


urlpatterns = [

    url( r'^info/$', views.hi, name='info_url' ),

    url( r'^regular_web_response/$', views.response_regular, name='response_regular_url' ),
    url( r'^channels_web_response/$', views.response_channels, name='response_channels_url' ),

    url( r'^$',  RedirectView.as_view(pattern_name='web:info_url') ),

    ]
