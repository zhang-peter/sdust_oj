# coding=utf8

from sqlalchemy import *
from sqlalchemy.orm import relation, relationship

from sdust_oj.sa_conn import DeclarativeBase, metadata, Session

problemCCGC = Table(u'problemCCGC', metadata,
    Column(u'problem_id', INTEGER(), ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column(u'ccgc_id', INTEGER(), ForeignKey('CompilableCodeGenerationConfig.id'), primary_key=True, nullable=False),
)

problemCompileConfig = Table(u'problemCompileConfig', metadata,
    Column(u'problem_id', INTEGER(), ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column(u'compileconfig_id', INTEGER(), ForeignKey('CompileConfig.id'), primary_key=True, nullable=False),
)

problemIOData = Table(u'problemIOData', metadata,
    Column(u'problem_id', INTEGER(), ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column(u'io_id', INTEGER(), ForeignKey('InputOutputData.id'), primary_key=True, nullable=False),
)

problemKeywordCheckConfig = Table(u'problemKeywordCheckConfig', metadata,
    Column(u'keyconfig_id', INTEGER(), ForeignKey('KeywordCheckConfig.id'), primary_key=True, nullable=False),
    Column(u'problem_id', INTEGER(), ForeignKey('Problem.id'), primary_key=True, nullable=False),
)

problemOutputCheckConfig = Table(u'problemOutputCheckConfig', metadata,
    Column(u'problem_id', INTEGER(), ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column(u'outputcheck_id', INTEGER(), ForeignKey('OutputCheckConfig.id'), primary_key=True, nullable=False),
)

problemRunConfig = Table(u'problemRunConfig', metadata,
    Column(u'problem_id', INTEGER(), ForeignKey('Problem.id'), primary_key=True, nullable=False),
    Column(u'runconfig_id', INTEGER(), ForeignKey('RunConfig.id'), primary_key=True, nullable=False),
)

class CompilableCodeGenerationConfig(DeclarativeBase):
    __tablename__ = 'CompilableCodeGenerationConfig'

    __table_args__ = {}

    #column definitions
    code_type_id = Column(u'code_type_id', INTEGER())
    generation_method = Column(u'generation_method', VARCHAR(length=254))
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))
    requirment = Column(u'requirment', INTEGER())

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='CompilableCodeGenerationConfig.problem_meta_id==ProblemMeta.id')
    Problems = relation('Problem', primaryjoin='CompilableCodeGenerationConfig.id==problemCCGC.c.ccgc_id', secondary=problemCCGC, secondaryjoin='problemCCGC.c.problem_id==Problem.id')


class CompileConfig(DeclarativeBase):
    __tablename__ = 'CompileConfig'

    __table_args__ = {}

    #column definitions
    code_type = Column(u'code_type', INTEGER())
    config = Column(u'config', VARCHAR(length=254))
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='CompileConfig.problem_meta_id==ProblemMeta.id')
    problems = relationship('Problem', secondary=problemCompileConfig, backref="compile_configs")


class Description(DeclarativeBase):
    __tablename__ = 'Description'

    __table_args__ = {}

    #column definitions
    content = Column(u'content', VARCHAR(length=254))
    hint = Column(u'hint', VARCHAR(length=254))
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    input = Column(u'input', VARCHAR(length=254))
    output = Column(u'output', VARCHAR(length=254))
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))
    sample_input = Column(u'sample_input', VARCHAR(length=254))
    sample_output = Column(u'sample_output', VARCHAR(length=254))
    source = Column(u'source', VARCHAR(length=254))
    title = Column(u'title', VARCHAR(length=254))

    problems = relationship('Problem', backref="description")

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='Description.problem_meta_id==ProblemMeta.id')

class InputOutputData(DeclarativeBase):
    __tablename__ = 'InputOutputData'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    name = Column(u'name', VARCHAR(length=254))
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='InputOutputData.problem_meta_id==ProblemMeta.id')
    problems = relationship('Problem', secondary=problemIOData, backref="input_output_datas")


class KeywordCheckConfig(DeclarativeBase):
    __tablename__ = 'KeywordCheckConfig'

    __table_args__ = {}

    #column definitions
    code_type = Column(u'code_type', INTEGER())
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))
    word = Column(u'word', VARCHAR(length=254))

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='KeywordCheckConfig.problem_meta_id==ProblemMeta.id')
    Problems = relation('Problem', primaryjoin='KeywordCheckConfig.id==problemKeywordCheckConfig.c.keyconfig_id', secondary=problemKeywordCheckConfig, secondaryjoin='problemKeywordCheckConfig.c.problem_id==Problem.id')


class OutputCheckConfig(DeclarativeBase):
    __tablename__ = 'OutputCheckConfig'

    __table_args__ = {}

    #column definitions
    check_method = Column(u'check_method', VARCHAR(length=254))
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='OutputCheckConfig.problem_meta_id==ProblemMeta.id')
    problems = relationship('Problem', secondary=problemOutputCheckConfig, backref="output_check_configs")


class Problem(DeclarativeBase):
    __tablename__ = 'Problem'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    judge_flow = Column(u'judge_flow', VARCHAR(length=254))
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))
    description_id = Column(u'description_id', INTEGER(), ForeignKey('Description.id'))

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='Problem.problem_meta_id==ProblemMeta.id')
    CompilableCodeGenerationConfigs = relation('CompilableCodeGenerationConfig', primaryjoin='Problem.id==problemCCGC.c.problem_id', secondary=problemCCGC, secondaryjoin='problemCCGC.c.ccgc_id==CompilableCodeGenerationConfig.id')
    CompileConfigs = relation('CompileConfig', primaryjoin='Problem.id==problemCompileConfig.c.problem_id', secondary=problemCompileConfig, secondaryjoin='problemCompileConfig.c.compileconfig_id==CompileConfig.id')
    InputOutputDatas = relation('InputOutputData', primaryjoin='Problem.id==problemIOData.c.problem_id', secondary=problemIOData, secondaryjoin='problemIOData.c.io_id==InputOutputData.id')
    KeywordCheckConfigs = relation('KeywordCheckConfig', primaryjoin='Problem.id==problemKeywordCheckConfig.c.problem_id', secondary=problemKeywordCheckConfig, secondaryjoin='problemKeywordCheckConfig.c.keyconfig_id==KeywordCheckConfig.id')
    OutputCheckConfigs = relation('OutputCheckConfig', primaryjoin='Problem.id==problemOutputCheckConfig.c.problem_id', secondary=problemOutputCheckConfig, secondaryjoin='problemOutputCheckConfig.c.outputcheck_id==OutputCheckConfig.id')
    RunConfigs = relation('RunConfig', primaryjoin='Problem.id==problemRunConfig.c.problem_id', secondary=problemRunConfig, secondaryjoin='problemRunConfig.c.runconfig_id==RunConfig.id')

    def get_judge_flow(self):
        """
        返回列表
        """
        return get_judge_flow_name(self.judge_flow)
    
    def get_config_refer(self):
        judge_id_str = str(self.judge_flow)
        judge_id_strs = judge_id_str.split(JUDGE_FLOW_MARK_SEPARATOR)
        configs_refer = []
        
        for f in judge_flows:
            if str(f[0]) in judge_id_strs:
                    configs_refer.append(f[3])
        return configs_refer
    
    def get_config_list_template(self):
        judge_id_str = str(self.judge_flow)
        judge_id_strs = judge_id_str.split(JUDGE_FLOW_MARK_SEPARATOR)
        config_list_templates = []
        
        for f in judge_flows:
            if str(f[0]) in judge_id_strs:
                config_list_templates.append(JUDGE_FLOW_TEMPLATES_PATH + f[2] + "_problem_edit.html")
                    
        return config_list_templates

from sdust_oj.constant import JUDGE_FLOW_MARK_SEPARATOR, judge_flows,\
JUDGE_FLOW_TEMPLATES_PATH
from sdust_oj.utils import get_judge_flow_name
class ProblemMeta(DeclarativeBase):
    __tablename__ = 'ProblemMeta'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    judge_flow = Column(u'judge_flow', VARCHAR(length=254))
    title = Column(u'title', VARCHAR(length=254), nullable=False)

    #relation definitions
    descriptions = relationship("Description", backref="problem_meta")
    compile_configs = relationship("CompileConfig", backref="problem_meta")
    runtime_configs = relationship("RunConfig", backref="problem_meta")
    output_check_configs = relationship("OutputCheckConfig", backref="problem_meta")
    input_output_datas = relationship("InputOutputData", backref="problem_meta")
    problems = relationship("Problem", backref="problem_meta")
    
    def get_judge_flow(self):
        """
        返回列表
        """
        return get_judge_flow_name(self.judge_flow)
    
    def get_config_list_template(self):
        judge_id_str = str(self.judge_flow)
        judge_id_strs = judge_id_str.split(JUDGE_FLOW_MARK_SEPARATOR)
        config_list_templates = []
        
        for f in judge_flows:
            if str(f[0]) in judge_id_strs:
                config_list_templates.append(JUDGE_FLOW_TEMPLATES_PATH + f[2] + "_list.html")
                    
        return config_list_templates


    def get_config_refer(self):
        judge_id_str = str(self.judge_flow)
        judge_id_strs = judge_id_str.split(JUDGE_FLOW_MARK_SEPARATOR)
        configs_refer = []
        
        for f in judge_flows:
            if str(f[0]) in judge_id_strs:
                    configs_refer.append(f[3])
        return configs_refer

class RunConfig(DeclarativeBase):
    __tablename__ = 'RunConfig'

    __table_args__ = {}

    #column definitions
    code_type = Column(u'code_type', INTEGER())
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    memory = Column(u'memory', INTEGER())
    problem_meta_id = Column(u'problem_meta_id', INTEGER(), ForeignKey('ProblemMeta.id'))
    time = Column(u'time', INTEGER())

    #relation definitions
    ProblemMeta = relation('ProblemMeta', primaryjoin='RunConfig.problem_meta_id==ProblemMeta.id')
    problems = relationship('Problem', secondary=problemRunConfig, backref="runtime_configs")


class Submission(DeclarativeBase):
    __tablename__ = 'Submission'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    status = Column(u'status', INTEGER())
    sub_time = Column(u'sub_time', DATETIME())
    used_memory = Column(u'used_memory', INTEGER())
    used_time = Column(u'used_time', INTEGER())
    user_id = Column(u'user_id', INTEGER(), ForeignKey('User.id'))
    problem_id = Column(u'problem_id', INTEGER(), ForeignKey('Problem.id'))

    #relation definitions
    User = relation('User', primaryjoin='Submission.user_id==User.id')
    Problem = relation('Problem', primaryjoin='Submission.problem_id==Problem.id')
    
metadata.create_all()