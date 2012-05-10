from sdust_oj.problem.views import *
from django.conf.urls import patterns, url
from sdust_oj.problem.forms import *

urlpatterns = patterns('', 
    url(r'^$', problem_index, name="problem_index"),
    url(r'^meta_list/(?P<page>\d{,10})/$', meta_list, name="meta_list"),
    url(r'^meta_detail/(?P<meta_id>\d{,10})/$', meta_detail, name="meta_detail"),   
    url(r'^compilable_code_generation_config_add/(?P<meta_id>\d{,10})/$', meta_config_add ,{'configForm':CompilableCodeGenerationConfigForm}, name='compilable_code_generation_config_add'),
    url(r'^compile_config_add/(?P<meta_id>\d{,10})/$', meta_config_add, {'configForm':CompileConfigForm}, name='compile_config_add'),
    url(r'^description_add/(?P<meta_id>\d{,10})/$', meta_config_add, {'configForm':DescriptionForm}, name='description_add'),
    url(r'^input_output_data_add/(?P<meta_id>\d{,10})/$', meta_config_add, {'configForm':InputOutputDataForm}, name='input_output_data_add'),
    url(r'^keyword_checkconfig_add/(?P<meta_id>\d{,10})/$', meta_config_add, {'configForm':KeywordCheckConfigForm}, name='keyword_check_config_add'),
    url(r'^output_check_config_add/(?P<meta_id>\d{,10})/$', meta_config_add, {'configForm':OutputCheckConfigForm}, name='output_check_config_add'),
    url(r'^problem_add/(?P<meta_id>\d{,10})/$', meta_config_add, {'configForm':ProblemForm, 'redirect_to':"problem_config_edit"}, name='problem_add'),
    url(r'^problem_config_edit/(?P<id>\d{,10})/$', problem_config_edit, name='problem_config_edit'),
    url(r'^problem_meta_upload/$', meta_config_add, {'meta_id':None, 'configForm':ProblemMetaForm}, name='problem_meta_upload'),  
    url(r'^run_config_add/(?P<meta_id>\d{,10})/$', meta_config_add, {'configForm':RunConfigForm}, name='run_config_add'),              
    url(r'^submit_success/$', submit_success, name='submit_success'),
)
