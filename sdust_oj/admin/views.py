from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext

def admin_index(request):
	 return render_to_response("admin/admin_index.html",
							context_instance=RequestContext(request))    

