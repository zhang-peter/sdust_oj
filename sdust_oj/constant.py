# coding=utf8

'''
Created on May 8, 2012

@author: jingyong
'''

JUDGE_FLOW_MARK_SEPARATOR = "$" # 判定流程分隔符
JUDGE_FLOW_TEMPLATES_PATH = "problem/"

from sdust_oj import status as STATUS
judge_flows = [
   # 0:id  1:name           2: template         3:model refer              4: model name       5: Complete Status       6:Queue Flag
    (1, "Compile",      "compile_config",       "compile_configs",        "CompileConfig",     STATUS.compile_ok,          "Compiling"),
    (2, "Run",          "runtime_config",       "runtime_configs",        "RuntimeConfig",     STATUS.run_ok,              "Running"),
    (3, "Output Check", "output_check_config",  "output_check_configs" ,   "OutputCheckConfig",STATUS.output_check_ok,     "Output_checking"),
     ]

code_types = [
    # 0: id,   1: name             2: save code as file
    (  0,        "C",                     False),
    (  1,        "C++",                   False),
    (  2,        "Pascal",                False),
    (  3,        "Java",                  False),
    (  4,        "Ruby",                  False),
    (  5,        "Shell",                 False),
    (  6,        "Python",                False),
    (  7,        "PHP",                   False),
    (  8,        "Perl",                  False),
    (  9,        "C#",                    False),
    (  10,       "Code::Blocks",          True),
    (  11,       "VC++6.0",               True),
    ]

STATUS = [
    # 0: id,   1: name
    (  1,        "Pending"),
          ]