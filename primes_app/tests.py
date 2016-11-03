# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, pprint
from django.test import TestCase
from primes_app import lib


class IsPrimeTest( TestCase ):
    """ Tests lib.is_prime() """

    def test__known_prime( self ):
        """ Tests known prime num. """
        num = 29
        self.assertEqual(
            ( True, 29 ),
            lib.is_prime( num )
            )

