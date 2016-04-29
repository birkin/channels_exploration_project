# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime, json, logging, os, pprint
from django.conf import settings as project_settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .formstuff import InvitationForm

log = logging.getLogger(__name__)


def hi( request ):
    """ Returns simplest response. """
    now = datetime.datetime.now()
    log.debug( 'now, `{}`'.format(now) )
    rsp = HttpResponse( '<p>hi</p> <p>( {} )</p>'.format(now) )
    log.debug( 'rsp, `{}`'.format(rsp) )
    try:
        return rsp
    except Exception as e:
        log.error( 'exception, ```{}```'.format(unicode(repr(e))) )


def invite( request ):
    """ Shows invite form. Submission will eventually be handed off to channels. """
    if request.method == 'GET':
        form = InvitationForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = InvitationForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            log.debug( 'form is valid' )
            # content = form.cleaned_data['content']
            # created_at = form.cleaned_data['created_at']
            # post = m.Post.objects.create(content=content, created_at=created_at)
            # return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))

    return render(request, 'email_app_templates/invite.html', {
        'form': form,
    })



    now = datetime.datetime.now()
    return HttpResponse( '<p>invite coming</p> <p>( {} )</p>'.format(now) )
