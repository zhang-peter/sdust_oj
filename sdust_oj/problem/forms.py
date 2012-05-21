from django import forms
from sdust_oj.problem.models import CompilableCodeGenerationConfig, CompileConfig, Description,InputOutputData,\
    KeywordCheckConfig, OutputCheckConfig, Problem, ProblemMeta, RuntimeConfig,\
    Submission
from sdust_oj.sa_conn import Session
from django.utils.translation import ugettext, ugettext_lazy as _

class CompilableCodeGenerationConfigForm(forms.Form):   
    code_type = forms.ChoiceField(label=_('Code Type'), choices=())
    generation_method = forms.CharField(label=_("Generation method"), max_length = 254)    
    requirement = forms.IntegerField(label=_('requirement'))
    
    class Meta:
        model = CompilableCodeGenerationConfig
        
    def __init__(self, *args, **kwargs):
        super(CompilableCodeGenerationConfigForm, self).__init__(*args, **kwargs)
        self.fields['code_type'].choices = [(c[0], c[1]) for c in code_types]
                   
    def save(self, commit=True, meta_id=None):
        compilable_code_generation_config = CompilableCodeGenerationConfig() 
        compilable_code_generation_config.problem_meta_id = meta_id    
        compilable_code_generation_config.code_type = self.cleaned_data['code_type']
        compilable_code_generation_config.generation_method = self.cleaned_data['generation_method']  
        compilable_code_generation_config.requirement = self.cleaned_data['requirement']      
        
        session = Session()
        session.add(compilable_code_generation_config)
        session.commit()
        session.close()
        
        return  compilable_code_generation_config  

class CompileConfigForm(forms.Form):   
    code_type = forms.ChoiceField(label=_('Code Type'), choices=())
    config = forms.CharField(label=_("config"), max_length = 254)    

    class Meta:
        model = CompileConfig
        
    def __init__(self, *args, **kwargs):
        super(CompileConfigForm, self).__init__(*args, **kwargs)
        self.fields['code_type'].choices = [(c[0], c[1]) for c in code_types]
        
    def save(self, commit=True, meta_id=None):
        compile_config = CompileConfig() 
        compile_config.problem_meta_id = meta_id      
        compile_config.code_type = self.cleaned_data['code_type']
        compile_config.config = self.cleaned_data['config']        
        
        session = Session()
        session.add(compile_config)
        session.commit()
        session.close()
        
        return  compile_config

class DescriptionForm(forms.Form):
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
        
    def save(self, commit=True, meta_id=None, update=False, object_id=None):
        session = Session()
        if update:
            description = session.query(Description).get(int(object_id))
        else:
            description = Description()
        description.problem_meta_id = meta_id 
        description.title = self.cleaned_data['title']
        description.content = self.cleaned_data['content']
        description.input = self.cleaned_data['input']
        description.output = self.cleaned_data['output']
        description.sample_input = self.cleaned_data['sample_input']
        description.sample_output = self.cleaned_data['sample_output']
        description.hint = self.cleaned_data['hint']
        description.source = self.cleaned_data['source']               
        
        if not update:
            session.add(description)
        session.commit()
        session.close()
        
        return description

from sdust_oj.utils import save_io_file

class InputOutputDataForm(forms.Form):   
    name = forms.CharField(label=_("name"), max_length = 254)
    input_file = forms.FileField(label=_("input_file"), allow_empty_file=True)
    output_file = forms.FileField(label=_("output_file"), allow_empty_file=True)


    class Meta:
        model = InputOutputData
        
    def clean_input_file(self):
        input_file = self.cleaned_data['input_file']
        return self.check_file(input_file)
         
    def clean_output_file(self):
        output_file = self.cleaned_data['output_file']
        return self.check_file(output_file)
    
    def check_file(self, f):
        if f.size > 1024 * 1024 * 50:
            raise forms.ValidationError(_("File size should not be larger than 50MB!"))
        return f
        
    def save(self, commit=True, meta_id=None):
        input_output_data = InputOutputData() 
        input_output_data.problem_meta_id = meta_id   
        input_output_data.name = self.cleaned_data['name']
        input_file = self.cleaned_data['input_file']
        output_file = self.cleaned_data['output_file']
        
        session = Session()
        session.add(input_output_data)
        session.commit()        
        save_io_file(input_file, output_file, input_output_data)
        session.close()
        
        return input_output_data
        
class KeywordCheckConfigForm(forms.Form):    
    code_type = forms.ChoiceField(label=_('Code Type'), choices=())
    word = forms.CharField(label=_("word"), max_length = 254)

    class Meta:
        model = KeywordCheckConfig
        
    def __init__(self, *args, **kwargs):
        super(KeywordCheckConfigForm, self).__init__(*args, **kwargs)
        self.fields['code_type'].choices = [(c[0], c[1]) for c in code_types]
        
    def save(self, commit=True, meta_id=None):
        keyword_check_config = KeywordCheckConfig()
        keyword_check_config.problem_meta_id = meta_id
        keyword_check_config.code_type = self.cleaned_data['code_type']                
        keyword_check_config.word = self.cleaned_data['word']
        
        session = Session()
        session.add(keyword_check_config)
        session.commit()
        session.close()
        
        return  keyword_check_config


class OutputCheckConfigForm(forms.Form):   
    check_method = forms.CharField(label=_("check_method"), max_length = 254)    

    class Meta:
        model = OutputCheckConfig
        
    def save(self, commit=True, meta_id=None):
        output_check_config = OutputCheckConfig() 
        output_check_config.problem_meta_id = meta_id
        output_check_config.check_method = self.cleaned_data['check_method']   
        
        session = Session()
        session.add(output_check_config)
        session.commit()
        session.close()
        
        return  output_check_config

from sdust_oj.constant import judge_flows, JUDGE_FLOW_MARK_SEPARATOR
class ProblemMetaForm(forms.Form):
    title = forms.CharField(label=_('title'), max_length = 254)
    judge_flow = forms.CharField(label=('judge_flow'), max_length = 254)
    
    class Meta:
        model = ProblemMeta
        
    def clean_judge_flow(self):
        job_list = str(self.cleaned_data['judge_flow']).split(JUDGE_FLOW_MARK_SEPARATOR)
        avail_marks = [f[0] for f in judge_flows]
        for j in job_list:
            if job_list.count(j) > 1 or (int(j) not in avail_marks):
                raise forms.ValidationError(_("Illege Judge Flow!"))
                break;
        return self.cleaned_data['judge_flow']
        
                
    def save(self, commit=True):
        problem_meta = ProblemMeta()
        problem_meta.title = self.cleaned_data['title']
        job_list = self.cleaned_data['judge_flow']
        problem_meta.judge_flow = job_list
        session = Session()
        session.expire_on_commit = False
        session.add(problem_meta)
        session.commit()
        session.close()
        
        return problem_meta
        
class ProblemForm(forms.Form):
    judge_flow = forms.MultipleChoiceField(label=_('judge_flow'), choices=())
    
    class Meta:
        model = Problem
    def __init__(self, *args, **kwargs):
        super(ProblemForm, self).__init__(*args, **kwargs)
        session = Session()
        try:
            meta_id = int(args[0]["problem_meta_id"])
        except IndexError:
            meta_id = int(kwargs["initial"]["problem_meta_id"])
        except:
            session.close()
            return
        current_meta = session.query(ProblemMeta).get(meta_id)
        choices = []
        meta_flows = str(current_meta.judge_flow).split(JUDGE_FLOW_MARK_SEPARATOR)
        
        for j in meta_flows:
            for f in judge_flows:
                if str(f[0]) == j:
                    choices.append((f[0], f[1]))

        self.fields['judge_flow'].choices = choices
        
        session.close()
         
    def save(self, commit=True, meta_id=None):
        problem = Problem()
        problem.problem_meta_id = meta_id
        job_list = self.cleaned_data['judge_flow']
        flow_mark = ""
        for job in job_list:
            flow_mark += JUDGE_FLOW_MARK_SEPARATOR + str(job)
            
        problem.judge_flow = flow_mark
        session = Session()
        session.expire_on_commit = False
        session.add(problem)
        session.commit()
        session.close()
        
        return problem
            
class RuntimeConfigForm(forms.Form):   
    code_type = forms.ChoiceField(label=_('Code Type'), choices=())
    memory = forms.IntegerField(label=_('memory'))
    time = forms.IntegerField(label=_('time'))   
    
    def __init__(self, *args, **kwargs):
        super(RuntimeConfigForm, self).__init__(*args, **kwargs)
        self.fields['code_type'].choices = [(c[0], c[1]) for c in code_types]

    
    class Meta:
        model = RuntimeConfig
        
    def save(self, commit=True, meta_id=None):
        run_config = RuntimeConfig() 
        run_config.problem_meta_id = meta_id
        run_config.code_type = self.cleaned_data['code_type'] 
        run_config.memory = self.cleaned_data['memory'] 
        run_config.time = self.cleaned_data['time']   
        
        session = Session()
        session.add(run_config)
        session.commit()
        session.close()
        
        return  run_config

from sdust_oj.constant import code_types
from django.http import settings
import os
class SubmissionForm(forms.Form):
    code_type = forms.ChoiceField(label=_('Code Type'), choices=())
    code_text = forms.CharField(label=_('Code Text'), widget=forms.Textarea, required=False)
    code_file = forms.FileField(label=_('Code File'), required=False)
    
    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        self.fields['code_type'].choices = [(c[0], c[1]) for c in code_types]
    
    
    def clean_code_file(self):
        code_file = self.cleaned_data['code_file']
        return self.check_file(code_file)
    
    def check_file(self, f):
        if f is None:
            return None
        if f.size > 1024 * 1024:
            raise forms.ValidationError(_("File size should not be larger than 1024KB!"))
        if f.content_type not in ["application/x-zip-compressed", "application/zip"]:
            raise forms.ValidationError(_("Only zip file is allowed!"))
        
        return f
    
    def save(self, problem=None):
        if problem is None:
            return
        sub = Submission()
        sub.status = 1
        sub.problem_id = problem.id
        sub.code_type = self.cleaned_data["code_type"]
        sub.code = self.cleaned_data["code_text"]
        session = Session()
        session.add(sub)
        session.commit()
        self.handle_code(sub, self.cleaned_data["code_file"])
        session.close()
        
        return sub

    def handle_code(self, sub, code_file):
        save_file = False
        for c in code_types:
            if c[0] == sub.code_type:
                save_file = c[2]
                break
        if save_file is not True:
            return
        
        code_path = os.path.join(settings.JUDGE_ROOT, "data", str(sub.problem.problem_meta.id), "zipcode")
        if os.path.exists(code_path) is False:
            os.makedirs(code_path)
            
        f = open(os.path.join(code_path, "%d.zip" % sub.id), "wb+")
        if code_file is not None:
            for chunk in code_file.chunks():
                f.write(chunk)
        f.close()
        