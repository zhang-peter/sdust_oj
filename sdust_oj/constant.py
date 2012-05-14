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
    # 0: id,   1: name             2: save code as file
    (  1,        "C",                     False),
    (  2,        "C++",                   False),
    (  3,        "Java",                  False),
    (  4,        "Python",                False),
    (  5,        "PHP",                   False),
    (  6,        "Perl",                  False),
    (  9,        "Code::Blocks",          True),
    (  10,       "VC++6.0",               True),
    ]

STATUS = [
    # 0: id,   1: name
    (  1,        "Pending"),
          ]