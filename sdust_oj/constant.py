# coding=utf8

'''
Created on May 8, 2012

@author: jingyong
'''

JUDGE_FLOW_MARK_SEPARATOR = "$" # 判定流程分隔符
JUDGE_FLOW_TEMPLATES_PATH = "problem/"

judge_flows = [
   # 0:id  1:name           2: template         3:model refer              4: model name
    (1, "Compile",      "compile_config",       "compile_configs",        "CompileConfig"),
    (2, "Run",          "runtime_config",       "runtime_configs",        "RunConfig"),
    (3, "Output Check", "output_check_config",  "output_check_configs" ,   "OutputCheckConfig"),
     ]

code_types = [
    # 0: id,   1: name
    (  1,        "C"),
    (  2,        "C++"),
    (  3,        "Java"),
    (  4,        "Python"),
    (  5,        "PHP"),
    (  6,        "Perl"),
    (  9,        "Code::Blocks"),
    (  10,       "VC++6.0"),
    ]