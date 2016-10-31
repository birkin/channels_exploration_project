# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
For django channels controller (akin to views.py).
Activated by config/routing.py
"""

import logging, pprint, time
# from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.utils import timezone
from email_app.models import Invitation


# logger = logging.getLogger('email')
log = logging.getLogger(__name__)
log.debug( 'consumers.py loaded' )


def send_invite( message_obj ):
    log.debug( 'starting send_invite()' )
    time.sleep( 1 )
    try:
        log.debug( 'message_obj, `{}`'.format(message_obj) )
        log.debug( 'message_obj.__dict__, `{}`'.format(pprint.pformat(message_obj.__dict__)) )
        notification_dct = message_obj.content
        log.debug( 'notification_dct, `{}`'.format(notification_dct) )
        invite_key = notification_dct['key']
        log.debug( 'invite_key, `{}`'.format(invite_key) )
        invite = Invitation.objects.get( key=invite_key )
    except Exception as e:
        log.error( 'e, ```{}```'.format(unicode(repr(e))) )
        log.error("Invitation to send not found")
        return
    subject = "You've been invited!"
    body = "Go to https://%s/invites/accept/%s/ to join!" % (
            'foo',
            invite.key,
        )
    try:
        message = EmailMessage(
            subject=subject,
            body=body,
            from_email="from_email",
            to=[invite.email,],
        )
        message.send()
        invite.sent = timezone.now()
        invite.save()
    except:
        log.exception('Problem sending invite %s' % (invite.id))

# def send_invite(message):
#     log.debug( 'starting send_invite()' )
#     try:
#         invite = Invitation.objects.get(
#             id=message.content.get('id'),
#         )
#     except Invitation.DoesNotExist:
#         log.error("Invitation to send not found")
#         return

#     subject = "You've been invited!"
#     body = "Go to https://%s/invites/accept/%s/ to join!" % (
#             Site.objects.get_current().domain,
#             invite.key,
#         )
#     try:
#         message = EmailMessage(
#             subject=subject,
#             body=body,
#             from_email="from_email",
#             to=[invite.email,],
#         )
#         message.send()
#         invite.sent = timezone.now()
#         invite.save()
#     except:
#         log.exception('Problem sending invite %s' % (invite.id))
