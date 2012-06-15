from sdust_oj.problem.views import *
from django.conf.urls import patterns, url
from sdust_oj.problem.forms import *

urlpatterns = patterns('', 
    url(r'^$', problem_index, name="problem_index"),
    url(r'^meta_list/(?P<page>\d{,10})/$', meta_list, name="meta_list"),
    url(r'^meta_detail/(?P<meta_id>\d{,10})/$', meta_detail, name="meta_detail"),
    url(r'^meta_delete/(?P<meta_id>\d{,10})/$', meta_delete, name="meta_delete"),       
    url(r'^ccgc_add/(?P<meta_id>\d{,10})/$', meta_config_add,
        {'configForm':CompilableCodeGenerationConfigForm,
         'template_name':"problem/ccgc_add.html"},
         name='compilable_code_generation_config_add'),
    #url(r'^compile_config_edit/(?P<config_id>\d{,10})/$', compile_config_edit, name="compile_config_edit"),
    url(r'^compile_config_add/(?P<meta_id>\d{,10})/$', meta_config_add,
         {'configForm':CompileConfigForm, 'template_name':"problem/compile_config_add.html"}
         , name='compile_config_add'),
    url(r'^description_add/(?P<meta_id>\d{,10})/$', meta_config_add,
         {'configForm':DescriptionForm, "template_name":"problem/description_add.html"},
         name='description_add'),
    url(r'^input_output_data_add/(?P<meta_id>\d{,10})/$', meta_config_add,
         {'configForm':InputOutputDataForm, 'template_name':"problem/io_data_add.html"},
         name='input_output_data_add'),
    url(r'^keyword_check_config_add/(?P<meta_id>\d{,10})/$', meta_config_add,
         {'configForm':KeywordCheckConfigForm, 'template_name':"problem/keyword_check_config_add.html"},
         name='keyword_check_config_add'),
    url(r'^output_check_config_add/(?P<meta_id>\d{,10})/$', meta_config_add,
         {'configForm':OutputCheckConfigForm, 'template_name':"problem/output_check_config_add.html"},
         name='output_check_config_add'),
    url(r'^problem_add/(?P<meta_id>\d{,10})/$', meta_config_add,
         {'configForm':ProblemForm, 'redirect_to':"problem_config_edit", "template_name":"problem/problem_add.html"}, name='problem_add'),
    url(r'^problem_config_edit/(?P<id>\d{,10})/$', problem_config_edit, name='problem_config_edit'),
    url(r'^problem_meta_add/$', meta_add, name='problem_meta_add'),  
    url(r'^problem_meta_edit/(?P<meta_id>\d{,10})/$', meta_edit, name='meta_edit'),
    url(r'^runtime_config_add/(?P<meta_id>\d{,10})/$', meta_config_add,
         {'configForm':RuntimeConfigForm, "template_name":"problem/runtime_config_add.html"}, name='runtime_config_add'),    
    url(r'^submit_success/$', submit_success, name='submit_success'),
    
    url(r'^problem_list/(?P<page>\d{,10})/$', problem_list, name="problem_list"),
    url(r'^problem_list_admin/(?P<page>\d{,10})/$', problem_list_admin, name="problem_list_admin"),
    url(r'^problem_detail/(?P<prob_id>\d{,10})/$', problem_detail, name="problem_detail"),
    url(r'^problem_edit/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$', meta_config_edit,
        {'configForm':ProblemForm,'editObjectClass':Problem, "template_name":"problem/problem_add.html"},
        name='problem_edit'),  
    url(r'^problem_delete/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$',
             meta_config_delete, {'deleteObjectClass':Problem}, name='problem_delete'),      
           
    
    url(r'^submit/(?P<prob_id>\d{,10})/$', submit, name="submit"),
    url(r'^status/(?P<page>\d{,10})/$', status, name="status"),
    
    url(r'^description_detail/(?P<object_id>\d{,10})/$', meta_config_detail,
        {'detailClass':Description,'template':'problem/description_detail.html'}, name="description_detail"),
    url(r'^description_delete/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$',
         meta_config_delete, {'deleteObjectClass':Description}, name='description_delete'),
    url(r'^description_edit/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$', meta_config_edit,
        {'configForm':DescriptionForm,'editObjectClass':Description, "template_name":"problem/description_add.html"},
        name='description_edit'),
    
    url(r'^io_data_delete/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$',
             meta_config_delete, {'deleteObjectClass':InputOutputData}, name='io_data_delete'), 
    url(r'^io_data_edit/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$', meta_config_edit,
        {'configForm':InputOutputDataForm,'editObjectClass':InputOutputData, "template_name":"problem/io_data_add.html"},
        name='io_data_edit'),
    
    url(r'^compile_config_delete/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$',
             meta_config_delete, {'deleteObjectClass':CompileConfig}, name='compile_config_delete'),      
    url(r'^compile_config_edit/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$', meta_config_edit,
        {'configForm':CompileConfigForm,'editObjectClass':CompileConfig, "template_name":"problem/compile_config_add.html"},
        name='compile_config_edit'),              
    
    url(r'^runtime_config_delete/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$',
             meta_config_delete, {'deleteObjectClass':RuntimeConfig}, name='runtime_config_delete'),      
    url(r'^runtime_config_edit/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$', meta_config_edit,
        {'configForm':RuntimeConfigForm,'editObjectClass':RuntimeConfig, "template_name":"problem/runtime_config_add.html"},
        name='runtime_config_edit'),
                       
    url(r'^output_check_config_delete/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$',
             meta_config_delete, {'deleteObjectClass':OutputCheckConfig}, name='output_check_config_delete'),      
    url(r'^output_check_config_edit/(?P<meta_id>\d{,10})/(?P<object_id>\d{,10})/$', meta_config_edit,
        {'configForm':OutputCheckConfigForm,'editObjectClass':OutputCheckConfig, "template_name":"problem/output_check_config_add.html"},
        name='output_check_config_edit'),
)
