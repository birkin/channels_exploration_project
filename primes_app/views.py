# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime, logging
from channels import Channel
from django.http import HttpResponse

log = logging.getLogger(__name__)


def hi( request ):
    """ Returns simplest response. """
    now = datetime.datetime.now()
    log.debug( 'now, `{}`'.format(now) )
    rsp = HttpResponse( '<p>hi</p> <p>( {} )</p>'.format(now) )
    log.debug( 'rsp, `{}`'.format(rsp) )
    try:
        return rsp
    except Exception as e:
        log.error( 'exception, ```{}```'.format(unicode(repr(e))) )


def regular_is_prime( request ):
    log.debug( 'starting response_regular()' )
    param = request.GET.get( 'foo', '' )
    if param:
        response_string = 'regular response -- {}'.format( param )
    else:
        response_string = 'regular response'
    return HttpResponse( response_string )


def channels_is_prime( request ):
    log.debug( 'starting response_channels()' )
    return HttpResponse( 'zz' )
    result = Channel('make-response').send( {'foo': 'bar'} )
    log.debug( 'type(result), `{}`'.format(type(result)) )
    return HttpResponse( result )

