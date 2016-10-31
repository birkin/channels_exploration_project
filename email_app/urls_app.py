# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import include, url
from django.views.generic import RedirectView
from email_app import views


urlpatterns = [

    url( r'^info/$', views.hi, name='info_url' ),

    url( r'^regular_invite/$', views.invite_regular, name='invite_regular_url' ),
    url( r'^channels_invite/$', views.invite_channels, name='invite_channels_url' ),

    url( r'^message/$', views.message, name='message_url' ),

    url( r'^$',  RedirectView.as_view(pattern_name='email:info_url') ),

    ]
