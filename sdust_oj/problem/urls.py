from sdust_oj.problem.views import *
from django.conf.urls import patterns, url
from sdust_oj.problem.forms import *

urlpatterns = patterns('',    
    url(r'^compilable_code_generation_config_upload/$', form_upload ,{'uploadForm':CompilableCodeGenerationConfigForm}, name='compilable_code_generation_config_upload'),
    url(r'^compile_config_upload/$', form_upload, {'uploadForm':CompileConfigForm}, name='compile_config_upload'),
    url(r'^description_upload/$', form_upload, {'uploadForm':DescriptionForm}, name='description_upload'),
    url(r'^input_output_data_upload/$', form_upload, {'uploadForm':InputOutputDataForm}, name='input_output_data_upload'),
    url(r'^keyword_checkconfig_upload/$', form_upload, {'uploadForm':KeywordCheckConfigForm}, name='keyword_checkconfig_upload'),
    url(r'^output_check_config_upload/$', form_upload, {'uploadForm':OutputCheckConfigForm}, name='output_check_config_upload'),
    url(r'^problem_upload/$', form_upload, {'uploadForm':ProblemForm}, name='problem_upload'),
    url(r'^problem_meta_upload/$', form_upload, {'uploadForm':ProblemMetaForm}, name='problem_meta_upload'),  
    url(r'^run_config_upload/$', form_upload, {'uploadForm':RunConfigForm}, name='run_config_upload'),              
    url(r'^submit_success/$', submit_success, name='submit_success'),
)
