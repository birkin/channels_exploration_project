# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('',

    url( r'^info/$',  'email_app.views.hi', name='info_url' ),

    url( r'^regular_invite/$',  'email_app.views.invite_regular', name='invite_regular_url' ),
    url( r'^channels_invite/$',  'email_app.views.invite_channels', name='invite_channels_url' ),

    url( r'^message/$',  'email_app.views.message', name='message_url' ),

    url( r'^$',  RedirectView.as_view(pattern_name='email:info_url') ),

    )
