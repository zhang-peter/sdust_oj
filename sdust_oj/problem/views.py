from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext

def submit_success(request):
	return render_to_response('problem/submit_success.html')

def form_upload(request,uploadForm):
    if request.method == 'POST':
        form = uploadForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submit_success'))
    else:
        form = uploadForm()    
    
    return render_to_response("problem/upload.html", {
        'form': form,}, context_instance=RequestContext(request))        

