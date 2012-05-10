from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from sdust_oj.problem.models import ProblemMeta, Problem
from sdust_oj.sa_conn import Session
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def problem_index(request):
    return render_to_response("problem/problem_index.html", context_instance=RequestContext(request))
    
from django.http import settings
def meta_list(request, page=1):
    session = Session()
    metas_all = session.query(ProblemMeta).all()
    session.close()
    
    paginator = Paginator(metas_all, settings.METAS_PER_PAGE)
    
    try:
         metas = paginator.page(metas_all)
    except (EmptyPage, InvalidPage):
        metas = paginator.page(paginator.num_pages)
    return render_to_response('problem/meta_list.html', {"metas": metas})

def meta_detail(request, meta_id):
    session = Session()
    meta = session.query(ProblemMeta).get(meta_id)
    if meta is None:
        raise Http404
    descriptions = meta.descriptions
    io_datas = meta.input_output_datas
    
    data = {"meta": meta,
            "descriptions": descriptions,
            "io_datas": io_datas}
    
    for config_refer in meta.get_config_refer():
        if hasattr(meta, config_refer):
            data.update({config_refer: getattr(meta, config_refer)})
            
    session.close()
    
    return render_to_response('problem/meta_detail.html', data)

def submit_success(request):
    return render_to_response('problem/submit_success.html')

def problem_config_edit(request, id):
    if request.method == 'POST':
        pass
    else:
        session = Session()
        problem = session.query(Problem).get(id)
#        desc_id = problem.description.id
#        meta_descs = problem.problem_meta.descriptions
        session.close()
        
        data = {'problem':problem,
                }
        
        return render_to_response("problem/problem_config_edit.html", data, context_instance=RequestContext(request)) 

def meta_config_add(request, meta_id, configForm, redirect_to=None):
    if request.method == 'POST':
        form = configForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save()
            if redirect_to is None:
                return HttpResponseRedirect(reverse('meta_detail', kwargs={'meta_id': meta_id}))
            else:
                return HttpResponseRedirect(reverse(redirect_to, kwargs={'id': obj.id}))
    else:
        form = configForm(initial={'problem_meta_id': meta_id})
    
    return render_to_response("problem/upload.html", {
        'form': form,}, context_instance=RequestContext(request)) 
    
    
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

