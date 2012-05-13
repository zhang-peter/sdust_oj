from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from sdust_oj.problem.models import ProblemMeta, Problem, Description, InputOutputData
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
from sqlalchemy.orm.collections import InstrumentedList
from sdust_oj.utils import get_model_by_model_ref, clear_sa_list
def problem_config_edit(request, id):
    if request.method == 'POST':
        desc_id = request.POST.get("desc_id", None)
        if desc_id is not None:
            try:
                desc_id = int(desc_id)
            except:
                desc_id = None
        session = Session()
        problem = session.query(Problem).get(id)
        if problem is None:
            session.close()
            raise Http404
        
        meta_id = problem.problem_meta_id
        if desc_id is None:
            problem.description = None
        else:
            description = session.query(Description).\
                filter_by(id=desc_id, problem_meta_id=problem.problem_meta_id).first()
            problem.description = description
            
        clear_sa_list(problem.input_output_datas)
        io_data_post = request.POST.getlist("io_datas", [])
        for io_data_id in io_data_post:
            io_data = session.query(InputOutputData).\
                filter_by(id=int(io_data_id), problem_meta_id=problem.problem_meta_id).first()
            if io_data is not None:
                problem.input_output_datas.append(io_data)
        session.commit()
            
        for config_refer in problem.get_config_refer():
            if hasattr(problem.problem_meta, config_refer) and \
               hasattr(problem, config_refer):
                configs = getattr(problem, config_refer)
                clear_sa_list(configs)
                configs_post = request.POST.getlist(config_refer, [])
                Model = get_model_by_model_ref(config_refer)
                for config_id in configs_post:
                    config = session.query(Model).\
                        filter_by(id=int(config_id), problem_meta_id=problem.problem_meta_id).first()
                    if config is not None:
                        configs.append(config)
                session.commit()
        session.commit()
        session.close()
    
        return HttpResponseRedirect(reverse('meta_detail', kwargs={'meta_id': meta_id}))
        
    else:
        session = Session()
        problem = session.query(Problem).get(id)
        
        if problem is None:
            session.close()
            raise Http404
        
        if problem.description is not None:
            desc_id = problem.description.id
        else:
            desc_id = -1
        meta_descs = problem.problem_meta.descriptions
        
        meta_io_datas = problem.problem_meta.input_output_datas
        io_datas_id = [data.id for data in problem.input_output_datas]
        
        data = {'problem':problem,
            'desc_id':desc_id,
            'meta_descs':meta_descs,
            'io_datas_id': io_datas_id,
            'meta_io_datas': meta_io_datas,
            }
        
        for config_refer in problem.get_config_refer():
            if hasattr(problem.problem_meta, config_refer):
                data.update({config_refer: getattr(problem.problem_meta, config_refer)})
            if hasattr(problem, config_refer):
                data.update({config_refer+"_id": [ c.id for c in getattr(problem, config_refer)]})
        
        session.close()
        
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


def problem_list(request, page=1):
    session = Session()
    prob_all = session.query(Problem).all()
    
    paginator = Paginator(prob_all, settings.METAS_PER_PAGE)
    
    try:
         probs = paginator.page(prob_all)
    except (EmptyPage, InvalidPage):
        probs = paginator.page(paginator.num_pages)
    res = render_to_response('problem/problem_list.html', {"probs": probs})
    session.close()
    
    return res

def problem_detail(request, prob_id):
    session = Session()
    prob = session.query(Problem).get(int(prob_id))
    if prob is None:
        session.close()
        raise Http404
    res = render_to_response('problem/problem_detail.html', {"prob": prob})
    session.close()
    return res

from forms import SubmissionForm
def submit(request, prob_id):
    session = Session()
    prob = session.query(Problem).get(int(prob_id))
    if request.method == "POST":
        pass
    else:
        form = SubmissionForm()
        res = render_to_response('problem/submit.html', {"prob": prob, "form": form})
    session.close()
    return res