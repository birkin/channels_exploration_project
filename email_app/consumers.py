# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
For django channels controller (akin to views.py).
Activated by config/routing.py
"""

import logging
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.utils import timezone
from invitations.models import Invitation


# logger = logging.getLogger('email')
log = logging.getLogger(__name__)


def send_invite(message):
    try:
        invite = Invitation.objects.get(
            id=message.content.get('id'),
        )
    except Invitation.DoesNotExist:
        logger.error("Invitation to send not found")
        return

    subject = "You've been invited!"
    body = "Go to https://%s/invites/accept/%s/ to join!" % (
            Site.objects.get_current().domain,
            invite.key,
        )
    try:
        message = EmailMessage(
            subject=subject,
            body=body,
            from_email="Invites <invites@%s.com>" % Site.objects.get_current().domain,
            to=[invite.email,],
        )
        message.send()
        invite.sent = timezone.now()
        invite.save()
    except:
        logger.exception('Problem sending invite %s' % (invite.id))
