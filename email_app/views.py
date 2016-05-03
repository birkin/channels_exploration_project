# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime, json, logging, os, pprint
from django.conf import settings as project_settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .formstuff import InvitationForm

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


def invite( request ):
    """ Shows invite form. Submission will eventually be handed off to channels. """
    if request.method == 'GET':
        invite_form = InvitationForm()
    else:
        invite_form = InvitationForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if invite_form.is_valid():
            log.debug( 'form is valid' )
            model_instance = invite_form.save()
            return HttpResponseRedirect( reverse('message_url') )
            # return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
    return render(  # gets here on GET or error
        request, 'email_app_templates/invite.html', {'form': invite_form,}
        )


def message( request ):
    """ Displays success message. """
    return HttpResponse( 'invitation sent' )
