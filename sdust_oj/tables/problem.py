# coding=UTF8

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean, \
    DateTime, Text
from sqlalchemy.orm import mapper, relationship
from datetime import datetime

from sdust_oj.sa_conn import metadata

problem_meta = Table("ProblemMeta", metadata,
                     Column("id", Integer, primary_key=True), 
                     Column("judge_flow", String(200), nullable=False, default=""),
                     Column("title", String(200), nullable=False, default="")
               )

problem = Table("Problem", metadata,
                Column("id", Integer, primary_key=True),
                Column("judge_flow", String(200), nullable=False, default=""),
                Column("problem_meta_id", Integer, ForeignKey('ProblemMeta.id')),
                Column("description_id", Integer, ForeignKey('Description.id')),
                Column("submit", Integer, nullable=False, default=0),
                Column("accept", Integer, nullable=False, default=0)
          )

description = Table("Description", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("problem_meta_id", Integer, ForeignKey('ProblemMeta.id')),
                    Column("title", String(200), nullable=False, default=""),
                    Column("content", Text, nullable=False, default=""),
                    Column("input", Text, nullable=False, default=""),
                    Column("output", Text, nullable=False, default=""),
                    Column("sample_input", Text, nullable=False, default=""),
                    Column("sample_output", Text, nullable=False, default=""),
                    Column("hint", Text, nullable=False, default=""),
                    Column("source", String(200), nullable=False, default=""),
              )

compile_config = Table("CompileConfig", metadata,
                       Column("id", Integer, primary_key=True),
                       Column("problem_meta_id", Integer, ForeignKey("ProblemMeta.id")),
                       Column("code_type", Integer, nullable=False, default=0),
                       Column("config", String(200), nullable=False, default="")
                 )

runtime_config = Table("RuntimeConfig", metadata,
                       Column("id", Integer, primary_key=True),
                       Column("problem_meta_id", Integer, ForeignKey("ProblemMeta.id")),
                       Column("code_type", Integer, nullable=False, default=0),
                       Column("memory", Integer, nullable=False, default=0),
                       Column("time", Integer, nullable=False, default=0),
                 )

output_check_config = Table("OutputCheckConfig", metadata,
                            Column("id", Integer, primary_key=True),
                            Column("problem_meta_id", Integer, ForeignKey("ProblemMeta.id")),
                            Column("check_method", String(200), nullable=False, default="")
                      )

input_output_data = Table("InputOutputData", metadata,
                            Column("id", Integer, primary_key=True),
                            Column("problem_meta_id", Integer, ForeignKey("ProblemMeta.id")),
                            Column("name", String(200), nullable=False, default="")
                    )

compilable_code_generation_config = Table("CompilableCodeGenerationConfig", metadata,
                       Column("id", Integer, primary_key=True),
                       Column("problem_meta_id", Integer, ForeignKey("ProblemMeta.id")),
                       Column("code_type", Integer, nullable=False, default=0),
                       Column("generation_method", String(200), nullable=False, default=""),
                       Column("requirement", Integer, nullable=False, default=0),
                 )

keyword_check_config = Table("KeywordCheckConfig", metadata,
                       Column("id", Integer, primary_key=True),
                       Column("problem_meta_id", Integer, ForeignKey("ProblemMeta.id")),
                       Column("code_type", Integer, nullable=False, default=0),
                       Column("word", String(200), nullable=False, default=""),
                 )

submission = Table("Submission", metadata,
                   Column("id", Integer, primary_key=True),
                   Column("problem_id", Integer, ForeignKey("Problem.id")),
                   Column("status", Integer, nullable=False, default=0),
                   Column("sub_time", DateTime, nullable=False, default=datetime.now()),
                   Column("used_memory", Integer, nullable=False, default=0),
                   Column("used_time", Integer, nullable=False, default=0),
                   Column("user_id", Integer, ForeignKey('User.id')),
                   Column("code_type", Integer, nullable=False, default=0),
                   Column("code", Text, nullable=False, default=""),
                   Column("length", Integer, nullable=False, default=0),
             )

problemCCGC = Table("problemCCGC", metadata,
    Column("problem_id", Integer, ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column("ccgc_id", Integer, ForeignKey('CompilableCodeGenerationConfig.id'), primary_key=True, nullable=False),
)

problemCompileConfig = Table("problemCompileConfig", metadata,
    Column("problem_id", Integer, ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column("compileconfig_id", Integer, ForeignKey('CompileConfig.id'), primary_key=True, nullable=False),
)

problemIOData = Table("problemIOData", metadata,
    Column("problem_id", Integer, ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column("io_id", Integer, ForeignKey('InputOutputData.id'), primary_key=True, nullable=False),
)

problemKeywordCheckConfig = Table("problemKeywordCheckConfig", metadata,
    Column("keyconfig_id", Integer, ForeignKey('KeywordCheckConfig.id'), primary_key=True, nullable=False),
    Column("problem_id", Integer, ForeignKey('Problem.id'), primary_key=True, nullable=False),
)

problemOutputCheckConfig = Table("problemOutputCheckConfig", metadata,
    Column("problem_id", Integer, ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column("outputcheck_id", Integer, ForeignKey('OutputCheckConfig.id'), primary_key=True, nullable=False),
)

problemRuntimeConfig = Table("problemRuntimeConfig", metadata,
    Column("problem_id", Integer, ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column("runtime_config_id", Integer, ForeignKey('RuntimeConfig.id'), primary_key=True, nullable=False),
)

metadata.create_all()

from sdust_oj.models.problem import ProblemMeta, Problem, Description, CompileConfig, \
    RuntimeConfig, OutputCheckConfig, InputOutputData, CompilableCodeGenerationConfig,\
    Submission, KeywordCheckConfig
    
mapper(ProblemMeta, problem_meta, properties={
    "descriptions":relationship(Description, backref="problem_meta"),
    "compile_configs":relationship(CompileConfig, backref="problem_meta"),
    "runtime_configs":relationship(RuntimeConfig, backref="problem_meta"),
    "output_check_configs":relationship(OutputCheckConfig, backref="problem_meta"),
    "input_output_datas":relationship(InputOutputData, backref="problem_meta"),
    "problems":relationship(Problem, backref="problem_meta"),
})

mapper(Problem, problem, properties={
    "submissions":relationship(Submission, backref="problem")
})
mapper(Description, description, properties={
    "problems":relationship(Problem, backref="description")
})

mapper(CompileConfig, compile_config, properties={
    "problems":relationship(Problem, secondary=problemCompileConfig, backref="compile_configs"),
})

mapper(RuntimeConfig, runtime_config, properties={
    "problems":relationship(Problem, secondary=problemRuntimeConfig, backref="runtime_configs"),
})

mapper(OutputCheckConfig, output_check_config, properties={
    "problems":relationship(Problem, secondary=problemOutputCheckConfig, backref="output_check_configs"),
})

mapper(InputOutputData, input_output_data, properties={
    "problems":relationship(Problem, secondary=problemIOData, backref="input_output_datas"),
})

mapper(CompilableCodeGenerationConfig, compilable_code_generation_config, properties={
    "problems":relationship(Problem, secondary=problemCCGC, backref="ccgcs"),
})

mapper(KeywordCheckConfig, keyword_check_config, properties={
    "problems":relationship(Problem, secondary=problemKeywordCheckConfig, backref="keyword_check_configs"),
})

mapper(Submission, submission)

def get_ac_ratio(self):
    if self.submit == 0:
        return 0
    return self.accept * 100 / self.submit

Problem.get_ac_ratio = get_ac_ratio

from sdust_oj.utils import get_judge_flow_name
from sdust_oj.constant import JUDGE_FLOW_MARK_SEPARATOR, judge_flows,\
JUDGE_FLOW_TEMPLATES_PATH
def get_judge_flow(self):
    """
    返回列表
    """
    return get_judge_flow_name(self.judge_flow)

Problem.get_judge_flow = get_judge_flow

def get_config_refer(self):
    judge_id_str = str(self.judge_flow)
    judge_id_strs = judge_id_str.split(JUDGE_FLOW_MARK_SEPARATOR)
    configs_refer = []
    
    for f in judge_flows:
        if str(f[0]) in judge_id_strs:
                configs_refer.append(f[3])
    return configs_refer

Problem.get_config_refer = get_config_refer

def get_config_list_template(self, sufix):
    judge_id_str = str(self.judge_flow)
    judge_id_strs = judge_id_str.split(JUDGE_FLOW_MARK_SEPARATOR)
    config_list_templates = []
    
    for f in judge_flows:
        if str(f[0]) in judge_id_strs:
            config_list_templates.append(JUDGE_FLOW_TEMPLATES_PATH + f[2] + sufix)
                
    return config_list_templates

def get_edit_config_list_template(self):
    return get_config_list_template(self, "_problem_edit.html")

Problem.get_edit_config_list_template = get_edit_config_list_template


def get_display_config_list_template(self):
    return get_config_list_template(self, "_list.html")

ProblemMeta.get_judge_flow = get_judge_flow
ProblemMeta.get_display_config_list_template = get_display_config_list_template
ProblemMeta.get_config_refer = get_config_refer

from sdust_oj.constant import code_types as CT
def get_code_type_name(code_type):
    for ct in CT:
        if ct[0] == code_type:
            return ct[1]

def get_code_type(self):
    return get_code_type_name(self.code_type)

RuntimeConfig.get_code_type = get_code_type

from django.http import settings

import os
def on_delete(self):
    data_path = os.path.join(settings.JUDGE_ROOT, "data", str(self.problem_meta.id), "testdata")
    input_path = os.path.join(data_path, "%d.in" % self.id)
    if os.path.exists(input_path):
       os.remove(input_path) 
    output_path = os.path.join(data_path, "%d.out" % self.id)
    if os.path.exists(output_path):
       os.remove(output_path)
  
InputOutputData.on_delete = on_delete

from sdust_oj import status as STATUS 
def get_status_name(self):
    return STATUS.STATUS_WORD[self.status]
Submission.get_status_name = get_status_name
Submission.get_code_type = get_code_type

CompileConfig.get_code_type = get_code_type
