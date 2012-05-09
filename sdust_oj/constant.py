# coding=utf8

'''
Created on May 8, 2012

@author: jingyong
'''

JUDGE_FLOW_MARK_SEPARATOR = "$" # 判定流程分隔符
JUDGE_FLOW_TEMPLATES_PATH = "problem/"

judge_flows = [
   # 0:id  1:name           2:config list template         3:model refer  
    (1, "Compile",      "compile_config_list.html",       "compile_configs"),
    (2, "Run",          "runtime_config_list.html",       "runtime_configs"),
    (3, "Output Check", "output_check_config_list.html",  "output_check_configs"),
     ]