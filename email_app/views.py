# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime, json, logging, os, pprint
from .formstuff import InvitationForm, ChannelsInvitationForm
from django.conf import settings as project_settings
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

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


def invite_regular( request ):
    """ Shows and submits invite form. Sends email traditionally. """
    if request.method == 'GET':
        log.debug( 'in invite_regular() GET' )
        invite_form = InvitationForm()
    else:
        log.debug( 'in invite_regular() POST' )
        invite_form = InvitationForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if invite_form.is_valid():
            log.debug( 'regular form is valid' )
            invite_instance = invite_form.save( commit=False )
            user = User.objects.all()[0]
            invite_instance.sender = user
            invite_instance.sent = datetime.datetime.now()
            log.debug( 'about to hit regular `invite_instance.save()`' )
            invite_instance.save()
            return HttpResponseRedirect( reverse('email:message_url') )
    return render(  # gets here on GET or error
        request, 'email_app_templates/invite.html', {'form': invite_form,}
        )


def invite_channels( request ):
    """ Shows and submits invite form. Sends email via channels. """
    if request.method == 'GET':
        log.debug( 'in invite_channels() GET' )
        invite_form = ChannelsInvitationForm()
    else:
        log.debug( 'in invite_channels() POST' )
        invite_form = ChannelsInvitationForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if invite_form.is_valid():
            log.debug( 'channels form is valid' )
            invite_instance = invite_form.save( commit=False )
            log.debug( 'invite_instance.__dict__ after false save, ```{}```'.format(pprint.pformat(invite_instance.__dict__)) )
            user = User.objects.all()[0]
            invite_instance.sender = user
            invite_instance.sent = datetime.datetime.now()
            log.debug( 'about to hit channels `invite_instance.save()`' )
            invite_instance.save()
            log.debug( 'invite_instance.__dict__ after real save, ```{}```'.format(pprint.pformat(invite_instance.__dict__)) )
            log.debug( 'about to return redirect' )
            return HttpResponseRedirect( reverse('email:message_url') )
    return render(  # gets here on GET or error
        request, 'email_app_templates/invite.html', {'form': invite_form,}
        )


def message( request ):
    """ Displays success message. """
    return HttpResponse( 'invitation sent' )
