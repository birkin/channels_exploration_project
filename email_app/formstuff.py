# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Invitation
from django import forms
from django.utils.crypto import get_random_string


class InvitationForm( forms.ModelForm ):

    class Meta:
        model = Invitation
        fields = ['email']

    def save(self, *args, **kwargs):
        # self.instance.key = get_random_string(32).lower()
        self.instance.key = get_random_string( 32, allowed_chars='abcdefghjkmnpqrstuvwxyz23456789' )
        return super(InvitationForm, self).save(*args, **kwargs)
