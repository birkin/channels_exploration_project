# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Invitation
from channels import Channel
from django import forms
from django.utils.crypto import get_random_string


class InvitationForm( forms.ModelForm ):
    """ ModelForm not using channels. """

    class Meta:
        model = Invitation
        fields = ['email']

    def save(self, *args, **kwargs):
        self.instance.key = get_random_string( 32, allowed_chars='abcdefghjkmnpqrstuvwxyz23456789' )
        return super(InvitationForm, self).save(*args, **kwargs)

    # end class InvitationForm


class ChannelsInvitationForm( forms.ModelForm ):
    """ ModelForm using channels. """

    class Meta:
        model = Invitation
        fields = ['email']

    def save(self, *args, **kwargs):
        self.instance.key = get_random_string( 32, allowed_chars='abcdefghjkmnpqrstuvwxyz23456789' )
        response = super(ChannelsInvitationForm, self).save(*args, **kwargs)
        notification = {
            'id': self.instance.id,
        }
        Channel('send-invite').send(notification)
        return response
