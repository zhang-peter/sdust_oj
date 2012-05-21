'''
Created on May 10, 2012

@author: jingyong
'''

from django.http import settings
import os

def save_io_file(input_file, output_file, input_output_data):
    data_path = os.path.join(settings.JUDGE_ROOT, "data", str(input_output_data.problem_meta.id), "testdata")
    if os.path.exists(data_path) is False:
        os.makedirs(data_path)
    
    f = open(os.path.join(data_path, "%d.in" % input_output_data.id), "wb+")
    if input_file is not None:
        for chunk in input_file.chunks():
            f.write(chunk)
    f.close()
    
    f = open(os.path.join(data_path, "%d.out" % input_output_data.id), "wb+")
    if output_file is not None:
        for chunk in output_file.chunks():
            f.write(chunk)
    f.close()
    
from sdust_oj.constant import JUDGE_FLOW_MARK_SEPARATOR, judge_flows
def get_judge_flow_name(flow_with_sp):
    flow_with_sp = str(flow_with_sp)

    judge_id_strs = flow_with_sp.split(JUDGE_FLOW_MARK_SEPARATOR)
    judge_flow_str = []
    
    for judge_id in judge_id_strs:
        for f in judge_flows:
            if str(f[0]) == judge_id:
                judge_flow_str.append(f[1])
    
    return judge_flow_str

from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
def get_model_by_model_ref(ref):
    model_name = ""
    for f in judge_flows:
        if f[3] == ref:
            model_name = f[4]
            break
    try:
        mod = import_module("sdust_oj.problem.models")
    except ImportError, e:
        raise ImproperlyConfigured('Error importing problem model sdust_oj.problem.models: "%s"' % (e))
    except ValueError, e:
        raise ImproperlyConfigured('Error importing problem model.')
    try:
        model = getattr(mod, model_name)
    except AttributeError:
        raise ImproperlyConfigured('Module sdust_oj.problem.models does not define a "%s" model' % (model_name))
    
    return model

def clear_sa_list(sa_list):
    l = list(sa_list)
    for e in l:
        sa_list.remove(e)