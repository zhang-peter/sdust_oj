from django import forms
from sdust_oj.problem.models import CompilableCodeGenerationConfig, CompileConfig, Description,InputOutputData, KeywordCheckConfig, OutputCheckConfig, Problem, ProblemMeta, RunConfig
from sdust_oj.sa_conn import Session
from django.utils.translation import ugettext, ugettext_lazy as _

class CompilableCodeGenerationConfigForm(forms.Form):   
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ()) 
    code_type_id = forms.IntegerField(label=_('code_type_id'))
    generation_method = forms.CharField(label=_(" generation_method"), max_length = 254)    
    requirment = forms.IntegerField(label=_('requirment'))
    
    class Meta:
        model = CompilableCodeGenerationConfig
            
    def __init__(self, *args, **kwargs):
        super(CompilableCodeGenerationConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        compilable_code_generation_config = CompilableCodeGenerationConfig() 
        compilable_code_generation_config.problem_meta_id = self.cleaned_data['problem_meta_id']       
        compilable_code_generation_config.code_type_id = self.cleaned_data['code_type_id']
        compilable_code_generation_config.generation_method = self.cleaned_data['generation_method']  
        compilable_code_generation_config.requirment = self.cleaned_data['requirment']      
        
        session = Session()
        session.add(compilable_code_generation_config)
        session.commit()
        session.close()
        
        return  compilable_code_generation_config  

class CompileConfigForm(forms.Form):   
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ()) 
    code_type = forms.IntegerField(label=_('code_type'))
    config = forms.CharField(label=_("config"), max_length = 254)    

    class Meta:
        model = CompileConfig
            
    def __init__(self, *args, **kwargs):
        super(CompileConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        compile_config = CompileConfig() 
        compile_config.problem_meta_id = self.cleaned_data['problem_meta_id']       
        compile_config.code_type = self.cleaned_data['code_type']
        compile_config.config = self.cleaned_data['config']        
        
        session = Session()
        session.add(compile_config)
        session.commit()
        session.close()
        
        return  compile_config

class DescriptionForm(forms.Form):   
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ()) 
    title = forms.CharField(label=_("title"), max_length = 254)    
    content = forms.CharField(label=_("content"), max_length = 254)
    input = forms.CharField(label=_("input"), max_length = 254)
    output = forms.CharField(label=_("output"), max_length = 254)
    sample_input = forms.CharField(label=_("sample_input"), max_length = 254) 
    sample_output = forms.CharField(label=_("sample_output"), max_length = 254)    
    hint = forms.CharField(label=_("hint"), max_length = 254)
    source = forms.CharField(label=_("source"), max_length = 254)   

    class Meta:
        model = Description
            
    def __init__(self, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        description = Description() 
        description.problem_meta_id = self.cleaned_data['problem_meta_id']       
        description.title = self.cleaned_data['title']
        description.content = self.cleaned_data['content']
        description.input = self.cleaned_data['input']
        description.output = self.cleaned_data['output']
        description.sample_input = self.cleaned_data['sample_input']
        description.sample_output = self.cleaned_data['sample_output']
        description.hint = self.cleaned_data['hint']
        description.source = self.cleaned_data['source']               
        
        session = Session()
        session.add(description)
        session.commit()
        session.close()
        
        return  description

class InputOutputDataForm(forms.Form):   
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ()) 
    name = forms.CharField(label=_("name"), max_length = 254)    

    class Meta:
        model = InputOutputData
            
    def __init__(self, *args, **kwargs):
        super(InputOutputDataForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        input_output_data = InputOutputData() 
        input_output_data.problem_meta_id = self.cleaned_data['problem_meta_id']       
        input_output_data.name = self.cleaned_data['name']   
        
        session = Session()
        session.add(input_output_data)
        session.commit()
        session.close()
        
        return  input_output_data
        
class KeywordCheckConfigForm(forms.Form):    
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ())
    code_type = forms.IntegerField(label=_('code_type'))
    word = forms.CharField(label=_("word"), max_length = 254)

    class Meta:
        model = KeywordCheckConfig
            
    def __init__(self, *args, **kwargs):
        super(KeywordCheckConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        keyword_check_config = KeywordCheckConfig()
        #keyword_check_config.problem_meta_id = int(self.cleaned_data['problem_meta_id'][0])
        keyword_check_config.problem_meta_id = self.cleaned_data['problem_meta_id']
        keyword_check_config.code_type = self.cleaned_data['code_type']                
        keyword_check_config.word = self.cleaned_data['word']
        
        session = Session()
        session.add(keyword_check_config)
        session.commit()
        session.close()
        
        return  keyword_check_config


class OutputCheckConfigForm(forms.Form):   
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ()) 
    check_method = forms.CharField(label=_("check_method"), max_length = 254)    

    class Meta:
        model = OutputCheckConfig
            
    def __init__(self, *args, **kwargs):
        super(OutputCheckConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        output_check_config = OutputCheckConfig() 
        output_check_config.problem_meta_id = self.cleaned_data['problem_meta_id']       
        output_check_config.check_method = self.cleaned_data['check_method']   
        
        session = Session()
        session.add(output_check_config)
        session.commit()
        session.close()
        
        return  output_check_config

from sdust_oj.constant import judge_flows, JUDGE_FLOW_MARK_SEPARATOR
class ProblemMetaForm(forms.Form):
    title = forms.CharField(label=_('title'), max_length = 254)
    judge_flow = forms.MultipleChoiceField(label=_('judge_flow'), choices=())
    
    def __init__(self, *args, **kwargs):
        super(ProblemMetaForm, self).__init__(*args, **kwargs)
        self.fields['judge_flow'].choices = [(f[0], f[1]) for f in judge_flows]
    
    class Meta:
        model = ProblemMeta
                
    def save(self, commit=True):
        problem_meta = ProblemMeta()
        problem_meta.title = self.cleaned_data['title']
        job_list = self.cleaned_data['judge_flow']
        flow_mark = ""
        for job in job_list:
            flow_mark += JUDGE_FLOW_MARK_SEPARATOR + str(job)
            
        problem_meta.judge_flow = flow_mark
        session = Session()
        session.add(problem_meta)
        session.commit()
        session.close()
        
        return problem_meta
        
class ProblemForm(forms.Form):
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ())
    judge_flow = forms.CharField(label=_('judge_flow'), max_length = 254)
    
    class Meta:
        model = Problem
    def __init__(self, *args, **kwargs):
        super(ProblemForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        session.close()
         
    def save(self, commit=True):
        problem = Problem()
        problem.problem_meta_id = self.cleaned_data['problem_meta_id']
        problem.judge_flow = self.cleaned_data['judge_flow']
        
        session = Session()
        session.add(problem)
        session.commit()
        session.close()
        
        return problem
            
class RunConfigForm(forms.Form):   
    problem_meta_id = forms.ChoiceField(label=_('problem_meta_id'), choices = ()) 
    code_type = forms.IntegerField(label=_('code_type'))
    memory = forms.IntegerField(label=_('memory'))
    time = forms.IntegerField(label=_('time'))   
    
    class Meta:
        model = RunConfig
            
    def __init__(self, *args, **kwargs):
        super(RunConfigForm, self).__init__(*args, **kwargs)
        session = Session()
        self.fields['problem_meta_id'].choices = [('', '----------')] + [(pm.id, pm.title) for pm in session.query(ProblemMeta).all()]
        
    def save(self, commit=True):
        run_config = RunConfig() 
        run_config.problem_meta_id = self.cleaned_data['problem_meta_id']       
        run_config.code_type = self.cleaned_data['code_type'] 
        run_config.memory = self.cleaned_data['memory'] 
        run_config.time = self.cleaned_data['time']   
        
        session = Session()
        session.add(run_config)
        session.commit()
        session.close()
        
        return  run_config

