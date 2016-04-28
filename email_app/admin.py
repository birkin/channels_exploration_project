# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Invitation
from django.contrib import admin


class InvitationAdmin( admin.ModelAdmin ):
    date_hierarchy = 'sent'
    list_display = [ 'sent', 'sender', 'email' ]
    ordering = [ '-id' ]


admin.site.register( Invitation, InvitationAdmin )
