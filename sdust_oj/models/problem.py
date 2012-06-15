# coding=UTF8

class CompilableCodeGenerationConfig(object):

    def __init__(self, generation_method="", problem_meta_id=None,
                 requirement=0):
        self.generation_method = generation_method
        self.problem_meta_id = problem_meta_id
        self.requirement = requirement




class CompileConfig(object):

    def __init__(self, code_type=0, config="", problem_meta_id=None):
        self.code_type = code_type
        self.config = config
        self.problem_meta_id = problem_meta_id



class Description(object):

    def __init__(self, content="", hint="", output="", problem_meta_id=None,
                 sample_input="", sample_output="", source="", title=""):
        self.content = content
        self.hint = hint
        self.output = output
        self.problem_meta_id = problem_meta_id
        self.sample_input = sample_input
        self.sample_output = sample_output
        self.source = source
        self.title = title



class InputOutputData(object):

    def __init__(self, name=""):
        self.name = name




class KeywordCheckConfig(object):

    def __init__(self, code_type=0, problem_meta_id=None, word=""):
        self.code_type = code_type
        self.problem_meta_id = problem_meta_id
        self.word = word



class OutputCheckConfig(object):

    def __init__(self, check_method="", problem_meta_id=None):
        self.check_method = check_method
        self.problem_meta_id = problem_meta_id




class Problem(object):

    def __init__(self, judge_flow="", problem_meta_id=None,
                 description_id=None, submit=0, accept=0):
        self.judge_flow = judge_flow
        self.problem_meta_id = problem_meta_id
        self.description_id = description_id
        self.submit = submit
        self.accept = accept

class ProblemMeta(object):

    def __init__(self, judge_flow="", title=""):
        self.judge_flow = judge_flow
        self.title = title

class RuntimeConfig(object):

    def __init__(self, code_type=0, memory=0, problem_meta_id=None,
                 time=0):
        self.code_type = code_type
        self.memory = memory
        self.problem_meta_id = problem_meta_id
        self.time = time

from datetime import datetime
class Submission(object):

    def __init__(self, status=0, sub_time=datetime.now(), used_memory=0, used_time=0,
                 user_id=None, problem_id=None, code_type=0, code="", length=0):
        self.status = status
        self.sub_time = sub_time
        self.used_memory = used_memory
        self.used_time = used_time
        self.user_id = user_id
        self.problem_id = problem_id
        self.code_type = code_type
        self.code = code
        self.length = length
