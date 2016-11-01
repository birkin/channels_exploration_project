# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime, logging
# from channels.handler import AsgiHandler
from django.http import HttpResponse

log = logging.getLogger(__name__)
log.debug( 'consumers.py loaded' )


def make_response( message_obj ):
    log.debug( 'starting make_response()' )
    response = HttpResponse( 'Hello world' )
    return response
