# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime, json, logging, os, pprint
from django.conf import settings as project_settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponseRedirect

log = logging.getLogger(__name__)


class Invitation(models.Model):

    email = models.EmailField()
    sent = models.DateTimeField(null=True)
    sender = models.ForeignKey(User)
    key = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "{} invited {}".format(self.sender, self.email)
