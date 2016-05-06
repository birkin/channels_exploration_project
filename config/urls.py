# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView


admin.autodiscover()

urlpatterns = patterns('',

    url( r'^admin/', include(admin.site.urls) ),  # eg host/project_x/admin/

    url( r'^email_demo/', include('email_app.urls_app', namespace='email') ),

    url( r'^', include('email_app.urls_app') ),  # eg host/project_x/anything/

    url( r'^$',  RedirectView.as_view(pattern_name='email:info_url') ),

)
