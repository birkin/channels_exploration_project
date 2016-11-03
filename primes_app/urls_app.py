# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url
from django.views.generic import RedirectView
from primes_app import views


urlpatterns = [

    url( r'^info/$', views.hi, name='info_url' ),

    url( r'^regular_is_prime/$', views.regular_is_prime, name='regular_url' ),
    url( r'^channels_is_prime/$', views.channels_is_prime, name='channels_url' ),

    url( r'^$',  RedirectView.as_view(pattern_name='primes:info_url') ),

    ]
