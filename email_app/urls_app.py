# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('',

    url( r'^info/$',  'email_app.views.hi', name='info_url' ),

    url( r'^invite/$',  'email_app.views.invite', name='invite_url' ),

    url( r'^$',  RedirectView.as_view(pattern_name='email:info_url') ),

    )
