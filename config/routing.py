# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
For django channels routing (akin to urls.py).
Activated by config.settings.CHANNEL_LAYERS
"""

from channels.routing import route
from email_app.consumers import send_invite


channel_routing = [
    route( 'send-invite', send_invite ),
]
