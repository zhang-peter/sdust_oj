# Create your views here.

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.decorators import login_required

from sdust_oj.sa_conn import Session

@login_required
def user_info(request):
    return render_to_response('users/user_info.html',
                              context_instance=RequestContext(request))