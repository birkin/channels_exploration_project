# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
For django channels routing (akin to urls.py).
Activated by config.settings.CHANNEL_LAYERS
"""

import logging
from channels.routing import route
from email_app.consumers import send_invite
from web_response_app.consumers import make_response


log = logging.getLogger(__name__)


log.debug( 'about to load channel_routing' )
channel_routing = [
    # route( 'send-invite', send_invite ),
    route( 'make-response', make_response ),
]
