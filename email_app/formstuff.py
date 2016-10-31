# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging, pprint
from .models import Invitation
from channels import Channel
from django import forms
from django.utils.crypto import get_random_string


log = logging.getLogger(__name__)


class InvitationForm( forms.ModelForm ):
    """ ModelForm not using channels. """

    class Meta:
        model = Invitation
        fields = ['email']

    def save(self, *args, **kwargs):
        self.instance.key = get_random_string( 32, allowed_chars='abcdefghjkmnpqrstuvwxyz23456789' )
        invitation_instance = super(InvitationForm, self).save(*args, **kwargs)
        return invitation_instance

    # def save(self, *args, **kwargs):
    #     self.instance.key = get_random_string( 32, allowed_chars='abcdefghjkmnpqrstuvwxyz23456789' )
    #     return super(InvitationForm, self).save(*args, **kwargs)

    # end class InvitationForm


class ChannelsInvitationForm( forms.ModelForm ):
    """ ModelForm using channels. """

    class Meta:
        model = Invitation
        fields = ['email']

    def save(self, *args, **kwargs):
        log.debug( 'in ChannelsInvitationForm.save()' )
        self.instance.key = get_random_string( 32, allowed_chars='abcdefghjkmnpqrstuvwxyz23456789' )
        channel_invitation_instance = super(ChannelsInvitationForm, self).save(*args, **kwargs)
        log.debug( 'type(channel_invitation_instance), `{}`'.format(type(channel_invitation_instance)) )
        log.debug( 'channel_invitation_instance.__dict__, `{}`'.format(pprint.pformat(channel_invitation_instance.__dict__)) )
        notification_dct = { 'key': channel_invitation_instance.key }
        log.debug( 'notification_dct, `{}`'.format(notification_dct) )
        log.debug( 'about to hit `Channel.send()`, which should trigger config.routing to perceive the `send-invite` string and have email_app.consumers.send_invite() do work.' )
        Channel('send-invite').send( notification_dct )
        return channel_invitation_instance

    # def save(self, *args, **kwargs):
    #     log.debug( 'in ChannelsInvitationForm.save()' )
    #     self.instance.key = get_random_string( 32, allowed_chars='abcdefghjkmnpqrstuvwxyz23456789' )
    #     response = super(ChannelsInvitationForm, self).save(*args, **kwargs)
    #     log.debug( 'type(response), `{}`'.format(type(response)) )
    #     notification_dct = { 'id': self.instance.id }
    #     log.debug( 'notification_dct, `{}`'.format(notification_dct) )
    #     log.debug( 'about to hit `Channel.send()`, which should trigger config.routing to perceive the `send-invite` string and have email_app.consumers.send_invite() do work.' )
    #     Channel('send-invite').send( notification_dct )
    #     log.debug( 'in ChannelsInvitationForm.save(); about to return response of type, `{}`'.format(type(response)) )
    #     return response
