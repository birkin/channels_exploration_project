# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
import primer

log = logging.getLogger(__name__)


def is_prime( num ):
    lst = primer.sieve( num )  # list of primes up to num
    log.debug( 'lst, `{}`'.format(lst) )
    return 'foo'
