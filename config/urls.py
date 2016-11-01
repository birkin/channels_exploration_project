# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView


log = logging.getLogger(__name__)

admin.autodiscover()


log.debug( 'about to load urlpatterns' )
urlpatterns = [

    url( r'^admin/', include(admin.site.urls) ),  # eg host/project_x/admin/

    url( r'^email_demo/', include('email_app.urls_app', namespace='email') ),

    url( r'^web_response_demo/', include('web_response_app.urls_app', namespace='web') ),

    url( r'^', include('email_app.urls_app') ),  # eg host/project_x/anything/

    url( r'^$',  RedirectView.as_view(pattern_name='email:info_url') ),

]
